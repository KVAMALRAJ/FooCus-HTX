# CivitAI Model Manager
# Manages downloading models, checkpoints, and LoRAs from CivitAI

import os
import json
import requests
from typing import Optional, Dict, List, Tuple
from pathlib import Path
import modules.config
from tqdm import tqdm


class CivitAIManager:
    """Manager for CivitAI model downloads"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize CivitAI manager
        
        Args:
            api_key: CivitAI API key. If None, loads from config
        """
        self.api_key = api_key or modules.config.civitai_api_key
        self.api_base = "https://civitai.com/api/v1"
        
    def get_model_info(self, model_id: str) -> Optional[Dict]:
        """
        Get model information from CivitAI
        
        Args:
            model_id: CivitAI model ID
            
        Returns:
            Model information dictionary or None if failed
        """
        try:
            url = f"{self.api_base}/models/{model_id}"
            headers = {}
            if self.api_key:
                headers['Authorization'] = f'Bearer {self.api_key}'
            
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[CivitAI] Failed to get model info: {response.status_code}")
                return None
        except Exception as e:
            print(f"[CivitAI] Error getting model info: {e}")
            return None
    
    def get_model_version_info(self, version_id: str) -> Optional[Dict]:
        """
        Get specific model version information
        
        Args:
            version_id: CivitAI model version ID
            
        Returns:
            Version information dictionary or None if failed
        """
        try:
            url = f"{self.api_base}/model-versions/{version_id}"
            headers = {}
            if self.api_key:
                headers['Authorization'] = f'Bearer {self.api_key}'
            
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[CivitAI] Failed to get version info: {response.status_code}")
                return None
        except Exception as e:
            print(f"[CivitAI] Error getting version info: {e}")
            return None
    
    def determine_model_type(self, model_info: Dict) -> str:
        """
        Determine the model type from model info
        
        Args:
            model_info: Model information dictionary
            
        Returns:
            Model type: 'checkpoint', 'lora', 'embedding', 'vae', 'controlnet', etc.
        """
        model_type = model_info.get('type', '').lower()
        
        # Map CivitAI types to Fooocus folder structure
        type_mapping = {
            'checkpoint': 'checkpoints',
            'lora': 'loras',
            'locon': 'loras',
            'textualinversion': 'embeddings',
            'embedding': 'embeddings',
            'vae': 'vae',
            'controlnet': 'controlnet',
            'poses': 'controlnet',
            'upscaler': 'upscale_models'
        }
        
        return type_mapping.get(model_type, 'checkpoints')
    
    def get_target_folder(self, model_type: str) -> str:
        """
        Get the target folder path for a model type
        
        Args:
            model_type: Model type (checkpoints, loras, etc.)
            
        Returns:
            Absolute path to target folder
        """
        folder_mapping = {
            'checkpoints': modules.config.paths_checkpoints[0],
            'loras': modules.config.paths_loras[0],
            'embeddings': modules.config.path_embeddings,
            'vae': modules.config.path_vae,
            'controlnet': modules.config.path_controlnet,
            'upscale_models': modules.config.path_upscale_models
        }
        
        return folder_mapping.get(model_type, modules.config.paths_checkpoints[0])
    
    def download_model(self, model_id: str, version_id: Optional[str] = None, 
                       progress_callback=None) -> Tuple[bool, str]:
        """
        Download a model from CivitAI
        
        Args:
            model_id: CivitAI model ID
            version_id: Specific version ID (optional, uses latest if not provided)
            progress_callback: Callback function for progress updates
            
        Returns:
            Tuple of (success, message)
        """
        try:
            # Get model info
            if progress_callback:
                progress_callback(0, "Fetching model information...")
            
            model_info = self.get_model_info(model_id)
            if not model_info:
                return False, "Failed to fetch model information"
            
            model_name = model_info.get('name', 'Unknown')
            model_type = self.determine_model_type(model_info)
            
            # Get version info
            if version_id:
                version_info = self.get_model_version_info(version_id)
                if not version_info:
                    return False, "Failed to fetch version information"
            else:
                # Use latest version
                versions = model_info.get('modelVersions', [])
                if not versions:
                    return False, "No versions available for this model"
                version_info = versions[0]
            
            version_name = version_info.get('name', 'Unknown')
            
            # Get download file
            files = version_info.get('files', [])
            if not files:
                return False, "No files available for download"
            
            # Prefer primary file or first file
            download_file = None
            for f in files:
                if f.get('primary', False):
                    download_file = f
                    break
            if not download_file:
                download_file = files[0]
            
            download_url = download_file.get('downloadUrl')
            if not download_url:
                return False, "Download URL not found"
            
            file_name = download_file.get('name', f"{model_name}_{version_name}.safetensors")
            file_size = download_file.get('sizeKB', 0) * 1024
            
            # Add API key to download URL if available
            if self.api_key:
                separator = '&' if '?' in download_url else '?'
                download_url = f"{download_url}{separator}token={self.api_key}"
            
            # Determine target folder
            target_folder = self.get_target_folder(model_type)
            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, file_name)
            
            # Check if already exists
            if os.path.exists(target_path):
                return False, f"File already exists: {file_name}"
            
            # Download file
            if progress_callback:
                progress_callback(5, f"Downloading {file_name}...")
            
            response = requests.get(download_url, stream=True, timeout=300)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', file_size))
            downloaded = 0
            
            with open(target_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if progress_callback and total_size > 0:
                            progress = 5 + int((downloaded / total_size) * 90)
                            progress_callback(progress, f"Downloading... {downloaded // 1024 // 1024}MB / {total_size // 1024 // 1024}MB")
            
            if progress_callback:
                progress_callback(100, f"Download complete: {file_name}")
            
            return True, f"Successfully downloaded {file_name} to {model_type} folder"
            
        except requests.exceptions.Timeout:
            return False, "Download timeout - file might be too large or connection is slow"
        except requests.exceptions.RequestException as e:
            return False, f"Download error: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def list_downloaded_files(self, model_type: str = 'all') -> List[Dict[str, str]]:
        """
        List downloaded model files
        
        Args:
            model_type: Type to filter ('all', 'checkpoints', 'loras', etc.)
            
        Returns:
            List of file information dictionaries
        """
        files = []
        
        folders_to_check = {}
        if model_type == 'all':
            folders_to_check = {
                'Checkpoints': modules.config.paths_checkpoints[0],
                'LoRAs': modules.config.paths_loras[0],
                'Embeddings': modules.config.path_embeddings,
                'VAE': modules.config.path_vae,
                'ControlNet': modules.config.path_controlnet,
                'Upscale Models': modules.config.path_upscale_models
            }
        else:
            folder = self.get_target_folder(model_type)
            folders_to_check = {model_type.title(): folder}
        
        for category, folder_path in folders_to_check.items():
            if not os.path.exists(folder_path):
                continue
            
            try:
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        # Get file size
                        size = os.path.getsize(file_path)
                        size_mb = size / (1024 * 1024)
                        
                        files.append({
                            'category': category,
                            'name': file_name,
                            'size': f"{size_mb:.2f} MB",
                            'path': file_path
                        })
            except Exception as e:
                print(f"[CivitAI] Error listing files in {folder_path}: {e}")
        
        return sorted(files, key=lambda x: (x['category'], x['name']))
    
    def delete_model(self, file_path: str) -> Tuple[bool, str]:
        """
        Delete a downloaded model file
        
        Args:
            file_path: Full path to the file to delete
            
        Returns:
            Tuple of (success, message)
        """
        try:
            if not os.path.exists(file_path):
                return False, "File not found"
            
            os.remove(file_path)
            return True, "File deleted successfully"
        except Exception as e:
            return False, f"Error deleting file: {str(e)}"


# Global instance
_civitai_manager = None


def get_civitai_manager() -> CivitAIManager:
    """Get or create global CivitAI manager instance"""
    global _civitai_manager
    if _civitai_manager is None:
        _civitai_manager = CivitAIManager()
    return _civitai_manager

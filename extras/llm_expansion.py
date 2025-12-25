# External LLM-based Prompt Expansion
# Supports DeepSeek API for enhanced prompt expansion

import os
import requests
from typing import Optional


def safe_str(x):
    """Safely convert to string and clean up whitespace"""
    x = str(x)
    for _ in range(16):
        x = x.replace('  ', ' ')
    return x.strip(",. \r\n")


class ExternalLLMExpansion:
    """
    External LLM-based prompt expansion using DeepSeek API
    """
    
    def __init__(self, api_key: Optional[str] = None, api_base: Optional[str] = None):
        """
        Initialize the external LLM expansion engine
        
        Args:
            api_key: DeepSeek API key. If None, will try to load from config
            api_base: DeepSeek API base URL. Defaults to https://api.deepseek.com
        """
        # Get API credentials from parameters or config
        import modules.config
        
        self.api_key = api_key or modules.config.deepseek_api_key
        self.api_base = api_base or modules.config.deepseek_api_base
        
        if not self.api_key or self.api_key == '':
            print('[External LLM Expansion] Warning: deepseek_api_key not found in config.txt. External expansion will not work.')
            print('[External LLM Expansion] Please add "deepseek_api_key": "your_key_here" to config.txt')
        else:
            print('[External LLM Expansion] DeepSeek API initialized successfully.')
    
    def is_available(self) -> bool:
        """Check if the external LLM expansion is available"""
        return bool(self.api_key)
    
    def expand_prompt(self, prompt: str, seed: int = 0) -> str:
        """
        Expand a prompt using DeepSeek API
        
        Args:
            prompt: The original prompt to expand
            seed: Random seed (not used with API but kept for compatibility)
            
        Returns:
            Expanded prompt string
        """
        if not self.is_available():
            print('[External LLM Expansion] API key not available, returning original prompt')
            return prompt
        
        if not prompt or prompt.strip() == '':
            return ''
        
        try:
            # Prepare the system message
            system_message = """You are an expert at expanding stable diffusion prompts. 
Your task is to take a short image generation prompt and expand it into a detailed, high-quality prompt that will generate better images.

Guidelines:
- Add artistic and technical details (lighting, composition, style, mood)
- Include quality enhancers (highly detailed, masterpiece, best quality, 8k, etc.)
- Maintain the core concept of the original prompt
- Keep it concise but descriptive (aim for 50-100 words)
- Use comma-separated descriptive phrases
- Do NOT add any explanations or commentary, ONLY return the expanded prompt
- Focus on visual details that improve image quality

Example:
Input: "a cat"
Output: "a highly detailed cat, professional photography, natural lighting, detailed fur texture, sharp focus, high resolution, photorealistic, masterpiece quality, sitting pose, warm colors, soft bokeh background"
"""
            
            # Prepare the API request
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': 'deepseek-chat',
                'messages': [
                    {'role': 'system', 'content': system_message},
                    {'role': 'user', 'content': f'Expand this image generation prompt: {prompt}'}
                ],
                'temperature': 0.7,
                'max_tokens': 200
            }
            
            # Make the API request
            response = requests.post(
                f'{self.api_base}/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                expanded = result['choices'][0]['message']['content'].strip()
                expanded = safe_str(expanded)
                
                # Remove any quotes that might wrap the response
                if expanded.startswith('"') and expanded.endswith('"'):
                    expanded = expanded[1:-1]
                if expanded.startswith("'") and expanded.endswith("'"):
                    expanded = expanded[1:-1]
                
                print(f'[External LLM Expansion] Original: {prompt}')
                print(f'[External LLM Expansion] Expanded: {expanded}')
                return expanded
            else:
                print(f'[External LLM Expansion] API error {response.status_code}: {response.text}')
                return prompt
                
        except requests.exceptions.Timeout:
            print('[External LLM Expansion] Request timeout, using original prompt')
            return prompt
        except Exception as e:
            print(f'[External LLM Expansion] Error during expansion: {e}')
            return prompt
    
    def __call__(self, prompt: str, seed: int = 0) -> str:
        """
        Callable interface for compatibility with FooocusExpansion
        
        Args:
            prompt: The original prompt to expand
            seed: Random seed (kept for compatibility)
            
        Returns:
            Expanded prompt string
        """
        return self.expand_prompt(prompt, seed)


# Global instance
_external_expansion_instance = None


def get_external_expansion():
    """Get or create the global external expansion instance"""
    global _external_expansion_instance
    if _external_expansion_instance is None:
        _external_expansion_instance = ExternalLLMExpansion()
    return _external_expansion_instance

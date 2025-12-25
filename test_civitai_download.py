#!/usr/bin/env python3
"""
Test script for CivitAI download functionality
Tests the same version IDs shown in user's wget examples
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from modules.civitai_manager import CivitAIManager
import modules.config

def test_download():
    """Test downloading a model using version ID"""
    
    print("=" * 60)
    print("CivitAI Download Test")
    print("=" * 60)
    
    # Initialize manager
    manager = CivitAIManager()
    
    # Test with the checkpoint version ID from user's example
    version_id = "2391289"  # CyberRealystic
    filename = "CyberRealystic.safetensors"
    
    print(f"\nTest 1: Download checkpoint")
    print(f"Version ID: {version_id}")
    print(f"Filename: {filename}")
    print(f"API Key configured: {'Yes' if manager.api_key else 'No'}")
    
    def progress_callback(progress, message):
        print(f"[{progress}%] {message}")
    
    print("\nAttempting download...\n")
    success, message = manager.download_model(
        version_id, 
        custom_filename=filename,
        progress_callback=progress_callback
    )
    
    print("\n" + "-" * 60)
    if success:
        print(f"✓ SUCCESS: {message}")
    else:
        print(f"✗ FAILED: {message}")
    print("-" * 60)
    
    # Test 2: LoRA download
    print(f"\n\nTest 2: Download LoRA")
    lora_version_id = "2267500"  # Indian_Clothing
    lora_filename = "Indian_Clothing.safetensors"
    
    print(f"Version ID: {lora_version_id}")
    print(f"Filename: {lora_filename}")
    
    print("\nAttempting download...\n")
    success2, message2 = manager.download_model(
        lora_version_id,
        custom_filename=lora_filename,
        progress_callback=progress_callback
    )
    
    print("\n" + "-" * 60)
    if success2:
        print(f"✓ SUCCESS: {message2}")
    else:
        print(f"✗ FAILED: {message2}")
    print("-" * 60)
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Checkpoint download: {'✓ PASSED' if success else '✗ FAILED'}")
    print(f"LoRA download: {'✓ PASSED' if success2 else '✗ FAILED'}")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_download()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()

#!/usr/bin/env python3
"""
Setup utilities for Kokoro Manim Voiceover
Handles model file downloads and installation prompts.
"""

import os
import sys
import urllib.request
from pathlib import Path
from typing import Tuple, Optional


def get_model_info() -> Tuple[str, str, str, str]:
    """Get model file information."""
    model_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx"
    voices_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin"
    model_file = "kokoro-v0_19.onnx"
    voices_file = "voices.bin"
    return model_url, voices_url, model_file, voices_file


def get_model_size_mb(url: str) -> int:
    """Get file size in MB from URL."""
    try:
        with urllib.request.urlopen(url) as response:
            size_bytes = int(response.headers.get('Content-Length', 0))
            return size_bytes // (1024 * 1024)
    except:
        return 0


def download_file_with_progress(url: str, filename: str) -> bool:
    """Download a file with progress indication."""
    try:
        def show_progress(block_num, block_size, total_size):
            if total_size > 0:
                downloaded = block_num * block_size
                percent = min(100, (downloaded * 100) // total_size)
                downloaded_mb = downloaded // (1024 * 1024)
                total_mb = total_size // (1024 * 1024)
                print(f"\r📥 Downloading {filename}... {percent}% ({downloaded_mb}MB/{total_mb}MB)", 
                      end="", flush=True)
        
        print(f"📥 Starting download of {filename}...")
        urllib.request.urlretrieve(url, filename, show_progress)
        print(f"\n✅ Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Failed to download {filename}: {e}")
        return False


def check_model_files() -> Tuple[bool, bool]:
    """Check if model files exist."""
    _, _, model_file, voices_file = get_model_info()
    model_exists = Path(model_file).exists()
    voices_exists = Path(voices_file).exists()
    return model_exists, voices_exists


def prompt_model_download() -> None:
    """Prompt user to download model files during installation."""
    print("\n" + "="*60)
    print("🎤 Kokoro Manim Voiceover - Model Files Setup")
    print("="*60)
    
    model_url, voices_url, model_file, voices_file = get_model_info()
    model_exists, voices_exists = check_model_files()
    
    if model_exists and voices_exists:
        print("✅ All model files are already present!")
        print("🚀 You're ready to use Kokoro Manim Voiceover!")
        return
    
    # Get file sizes
    model_size = get_model_size_mb(model_url)
    voices_size = get_model_size_mb(voices_url)
    total_size = model_size + voices_size
    
    print(f"📦 Model files required for Kokoro Manim Voiceover:")
    if not model_exists:
        print(f"   • {model_file} (~{model_size}MB)")
    if not voices_exists:
        print(f"   • {voices_file} (~{voices_size}MB)")
    print(f"   • Total download size: ~{total_size}MB")
    
    print(f"\n⚠️  These are large files that will be downloaded to your current directory.")
    print(f"   The files will be reused for future projects.")
    
    # Prompt user
    while True:
        response = input(f"\n🤔 Would you like to download the model files now? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            break
        elif response in ['n', 'no']:
            print(f"\n📝 Note: Model files will be downloaded automatically when you first use KokoroService.")
            print(f"   You can also run 'kokoro-mv-setup' later to download them manually.")
            return
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    # Download files
    print(f"\n🚀 Starting downloads...")
    success = True
    
    if not model_exists:
        success &= download_file_with_progress(model_url, model_file)
    
    if not voices_exists:
        success &= download_file_with_progress(voices_url, voices_file)
    
    if success:
        print(f"\n🎉 All model files downloaded successfully!")
        print(f"🚀 Kokoro Manim Voiceover is ready to use!")
    else:
        print(f"\n⚠️  Some downloads failed. You can try again later or download manually.")
        print(f"   Run 'kokoro-mv-setup' to retry the download process.")


def main():
    """Main function for the setup script."""
    try:
        prompt_model_download()
    except KeyboardInterrupt:
        print(f"\n\n⏹️  Setup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

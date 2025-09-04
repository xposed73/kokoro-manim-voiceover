#!/usr/bin/env python3
"""
Installation script for Kokoro Manim Voiceover
This script helps users install the package and its dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible!")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible!")
        print("Please use Python 3.11 or higher.")
        return False


def install_dependencies():
    """Install required dependencies."""
    return run_command("pip install -r requirements.txt", "Installing dependencies")


def install_package():
    """Install the package in development mode."""
    return run_command("pip install -e .", "Installing package in development mode")


def check_model_files():
    """Check if required model files are present."""
    model_files = ["kokoro-v0_19.onnx", "voices.bin"]
    missing_files = []
    
    for file in model_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"\n📥 Model files will be auto-downloaded when needed: {', '.join(missing_files)}")
        print("No manual download required - KokoroService handles this automatically!")
        return True  # This is now OK since auto-download is available
    else:
        print("✅ All required model files are present!")
        return True


def test_installation():
    """Test if the installation works."""
    try:
        from kokoro_mv.koko import KokoroService
        print("✅ KokoroService imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Failed to import KokoroService: {e}")
        return False


def main():
    """Main installation process."""
    print("🚀 Kokoro Manim Voiceover Installation Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Installation failed at dependency installation step.")
        sys.exit(1)
    
    # Install package
    if not install_package():
        print("\n❌ Installation failed at package installation step.")
        sys.exit(1)
    
    # Check model files
    check_model_files()
    
    # Test installation
    if not test_installation():
        print("\n❌ Installation test failed.")
        sys.exit(1)
    
    print("\n🎉 Installation completed successfully!")
    print("\n📖 Next steps:")
    print("1. Run: python main.py")
    print("2. Or create your own Manim scene with KokoroService")
    print("3. Model files will be downloaded automatically when needed!")
    print("\n📚 Example usage:")
    print("manim main.py KokoExample")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script to help with PyPI publishing workflow.
This script provides commands for building, checking, and publishing to PyPI.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main function to handle PyPI publishing workflow."""
    if len(sys.argv) < 2:
        print("Usage: python publish.py <command>")
        print("\nAvailable commands:")
        print("  build     - Build the package")
        print("  check     - Check the built package")
        print("  test      - Upload to TestPyPI")
        print("  publish   - Upload to PyPI")
        print("  clean     - Clean build artifacts")
        print("  all       - Build, check, and prepare for publishing")
        return

    command = sys.argv[1].lower()
    
    if command == "build":
        run_command("python -m build", "Building package")
        
    elif command == "check":
        if not Path("dist").exists():
            print("❌ No dist directory found. Run 'build' first.")
            return
        run_command("twine check dist/*", "Checking package")
        
    elif command == "test":
        if not Path("dist").exists():
            print("❌ No dist directory found. Run 'build' first.")
            return
        print("\n🚀 Uploading to TestPyPI...")
        print("Make sure you have configured your TestPyPI credentials!")
        run_command("twine upload --repository testpypi dist/*", "Uploading to TestPyPI")
        
    elif command == "publish":
        if not Path("dist").exists():
            print("❌ No dist directory found. Run 'build' first.")
            return
        print("\n🚀 Uploading to PyPI...")
        print("Make sure you have configured your PyPI credentials!")
        confirm = input("Are you sure you want to publish to PyPI? (yes/no): ")
        if confirm.lower() == "yes":
            run_command("twine upload dist/*", "Uploading to PyPI")
        else:
            print("❌ Publishing cancelled.")
            
    elif command == "clean":
        run_command("Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue", 
                   "Cleaning build artifacts")
        
    elif command == "all":
        print("🚀 Running complete PyPI preparation workflow...")
        if not run_command("python -m build", "Building package"):
            return
        if not run_command("twine check dist/*", "Checking package"):
            return
        print("\n✅ Package is ready for publishing!")
        print("📦 Built files are in the 'dist' directory.")
        print("🔧 To publish to TestPyPI: python publish.py test")
        print("🚀 To publish to PyPI: python publish.py publish")
        
    else:
        print(f"❌ Unknown command: {command}")
        print("Run 'python publish.py' without arguments to see available commands.")


if __name__ == "__main__":
    main()

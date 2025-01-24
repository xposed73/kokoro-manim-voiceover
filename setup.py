from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import requests
from tqdm import tqdm  # Import tqdm for the progress bar

class CustomInstallCommand(install):
    """Custom installation command to download required files."""
    
    def run(self):
        # Run the standard installation process
        install.run(self)
        
        # URLs for the model and voices files
        model_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx"  # Replace with your actual URL
        voices_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin"  # Replace with your actual URL

        # Paths where the files will be saved
        model_path = os.path.join(self.install_lib, "kokoro-v0_19.onnx")
        voices_path = os.path.join(self.install_lib, "voices.bin")
        
        # Download the files with loading progress
        self.download_file(model_url, model_path)
        self.download_file(voices_url, voices_path)

    def download_file(self, url, dest_path):
        """Helper function to download files with a loading progress bar."""
        if not os.path.exists(dest_path):
            print(f"Downloading {url} to {dest_path}...")
            
            # Get the size of the file to display the progress bar
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            if response.status_code == 200:
                with open(dest_path, 'wb') as file:
                    # Use tqdm for a nice progress bar
                    for data in tqdm(response.iter_content(1024), 
                                     total=total_size // 1024, 
                                     unit='KB', 
                                     desc=f"Downloading {os.path.basename(dest_path)}"):
                        file.write(data)
                print(f"File downloaded to {dest_path}")
            else:
                print(f"Failed to download file from {url}. Status code: {response.status_code}")
        else:
            print(f"File already exists at {dest_path}. Skipping download.")

# Setup function
setup(
    name="kokoro-mv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.0',     # Adding requests for downloading files
        'tqdm>=4.0',         # Adding tqdm for loading progress
        'torch>=1.10',       # Example: PyTorch (if needed for the Kokoro-82M model)
        'manim>=0.16.0',     # Example: Manim library for animations
        'pyttsx3>=2.7',      # Example: TTS library (if you're using it for voice synthesis)
        'kokoro-onnx',  # Adding kokoro-onnx as a dependency
    ],
    test_suite="tests",
    author="Nadeem Khan",
    author_email="nadeemak755@gmail.com",
    description="Library for generating voiceover in manim using Kokoro-82M model",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xposed73/kokoro-mv",
    license="MIT",
    cmdclass={
        'install': CustomInstallCommand,  # Use custom install command to download files
    },
)

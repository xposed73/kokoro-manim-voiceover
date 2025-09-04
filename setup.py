#!/usr/bin/env python3
"""
Setup script for Kokoro Manim Voiceover
Handles package installation with optional model download prompts.
"""

import os
import sys
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        self._post_install()

    def _post_install(self):
        """Run post-installation tasks."""
        try:
            from kokoro_mv.setup import prompt_model_download
            prompt_model_download()
        except ImportError:
            # Package not yet installed, skip
            pass


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        self._post_install()

    def _post_install(self):
        """Run post-installation tasks."""
        try:
            from kokoro_mv.setup import prompt_model_download
            prompt_model_download()
        except ImportError:
            # Package not yet installed, skip
            pass


def read_readme():
    """Read the README file."""
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return ""


def read_requirements():
    """Read requirements from pyproject.toml."""
    requirements = [
        "kokoro-onnx>=0.3.6",
        "manim>=0.19.0",
        "manim-voiceover>=0.3.7",
        "soundfile>=0.13.0",
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "setuptools>=75.8.0",
        "tqdm>=4.64.0"
    ]
    return requirements


setup(
    name="kokoro-manim-voiceover",
    version="0.1.0",
    author="Nadeem Akhtar Khan",
    author_email="nadeemak755@gmail.com",
    description="Professional library for generating high-quality voiceovers in Manim animations using Kokoro-82M model",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/xposed73/kokoro-manim-voiceover",
    project_urls={
        "Homepage": "https://github.com/xposed73/kokoro-manim-voiceover",
        "Repository": "https://github.com/xposed73/kokoro-manim-voiceover",
        "Issues": "https://github.com/xposed73/kokoro-manim-voiceover/issues",
        "Documentation": "https://github.com/xposed73/kokoro-manim-voiceover#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=read_requirements(),
    keywords=["manim", "voiceover", "text-to-speech", "kokoro", "animation", "tts", "ai-voice"],
    entry_points={
        "console_scripts": [
            "kokoro-mv-setup=kokoro_mv.setup:main",
        ],
    },
    cmdclass={
        "install": PostInstallCommand,
        "develop": PostDevelopCommand,
    },
    include_package_data=True,
    zip_safe=False,
)
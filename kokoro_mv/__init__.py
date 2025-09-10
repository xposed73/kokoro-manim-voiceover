"""
Kokoro Manim Voiceover - Professional TTS Library for Manim Animations

A high-quality text-to-speech library that integrates seamlessly with Manim
animations using the Kokoro-82M model for natural-sounding voiceovers.

Author: Nadeem Akhtar Khan
License: MIT
Version: 0.1.1
"""

from .koko import KokoroService

__version__ = "0.1.1"
__author__ = "Nadeem Akhtar Khan"
__email__ = "nadeemak755@gmail.com"
__license__ = "MIT"
__description__ = "Professional library for generating high-quality voiceovers in Manim animations using Kokoro-82M model"

__all__ = [
    'KokoroService',
    '__version__',
    '__author__',
    '__email__',
    '__license__',
    '__description__'
]
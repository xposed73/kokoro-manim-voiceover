"""
Copyright (c) 2025 Xposed73
All rights reserved.
This file is part of the Manim Voiceover project.
"""

import hashlib
import json
import numpy as np
import os
import urllib.request
from pathlib import Path
from manim_voiceover.services.base import SpeechService
from kokoro_onnx import Kokoro
from manim_voiceover.helper import remove_bookmarks, wav2mp3
from scipy.io.wavfile import write as write_wav


class KokoroService(SpeechService):
    """Speech service class for kokoro_self (using text_to_speech via Kokoro ONNX)."""

    def __init__(self, engine=None, model_path: str = "", voices_path: str = "",
                 voice: str = '', speed: float = 1.0, lang: str = "en-us", **kwargs):
        
        # Auto-download model files if they don't exist
        model_path, voices_path = self._ensure_model_files(model_path, voices_path)
        
        self.kokoro = Kokoro(model_path, voices_path)
        self.voice = voice
        self.speed = speed
        self.lang = lang

        if engine is None:
            engine = self.text_to_speech  # Default to local function

        self.engine = engine
        super().__init__(**kwargs)

    def _ensure_model_files(self, model_path: str, voices_path: str):
        """Ensure model files exist, download them if missing."""
        # Default file names if not specified
        if not model_path:
            model_path = "kokoro-v0_19.onnx"
        if not voices_path:
            voices_path = "voices.bin"
        
        # Download model file if it doesn't exist
        if not os.path.exists(model_path):
            print(f"📥 Downloading model file: {model_path}")
            self._download_file(
                "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx",
                model_path
            )
        
        # Download voices file if it doesn't exist
        if not os.path.exists(voices_path):
            print(f"📥 Downloading voices file: {voices_path}")
            self._download_file(
                "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin",
                voices_path
            )
        
        return model_path, voices_path
    
    def _download_file(self, url: str, filename: str):
        """Download a file from URL with progress indication."""
        try:
            def show_progress(block_num, block_size, total_size):
                downloaded = block_num * block_size
                if total_size > 0:
                    percent = min(100, (downloaded * 100) // total_size)
                    print(f"\r📥 Downloading... {percent}% ({downloaded // 1024 // 1024}MB/{total_size // 1024 // 1024}MB)", end="", flush=True)
            
            urllib.request.urlretrieve(url, filename, show_progress)
            print(f"\n✅ Downloaded: {filename}")
        except Exception as e:
            print(f"\n❌ Failed to download {filename}: {e}")
            raise

    def get_data_hash(self, input_data: dict) -> str:
        """
        Generates a hash based on the input data dictionary.
        The hash is used to create a unique identifier for the input data.

        Parameters:
            input_data (dict): A dictionary of input data (e.g., text, voice, etc.).

        Returns:
            str: The generated hash as a string.
        """
        # Convert the input data dictionary to a JSON string (sorted for consistency)
        data_str = json.dumps(input_data, sort_keys=True)
        # Generate a SHA-256 hash of the JSON string
        return hashlib.sha256(data_str.encode('utf-8')).hexdigest()

    import numpy as np

    def text_to_speech(self, text, output_file, voice_name, speed, lang):
        """
        Generates speech from text using Kokoro ONNX and saves the audio file.
        Normalizes the audio to make it audible.
        """
        # Generate audio samples using Kokoro
        samples, sample_rate = self.kokoro.create(
            text, voice=voice_name, speed=speed, lang=lang
        )

        # Normalize audio to the range [-1, 1]
        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples = samples / max_val

        # Convert to 16-bit integer PCM format
        samples = (samples * 32767).astype("int16")

        # Save the normalized audio as a .wav file
        write_wav(output_file, sample_rate, samples)
        print(f"Saved at {output_file}")

        return output_file


    def generate_from_text(self, text: str, cache_dir: str = None, path: str = None) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_data = {"input_text": text, "service": "kokoro_self", "voice": self.voice, "lang": self.lang}
        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_data_hash(input_data) + ".mp3"
        else:
            audio_path = path

        # Generate .wav file using the text_to_speech function
        audio_path_wav = str(Path(cache_dir) / audio_path.replace(".mp3", ".wav"))
        self.engine(
            text=text,
            output_file=audio_path_wav,
            voice_name=self.voice,
            speed=self.speed,
            lang=self.lang,
        )

        # Convert .wav to .mp3
        mp3_audio_path = str(Path(cache_dir) / audio_path)
        wav2mp3(audio_path_wav, mp3_audio_path)

        # Remove original .wav file
        remove_bookmarks(audio_path_wav)

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict

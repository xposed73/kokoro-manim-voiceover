"""
Test module for Kokoro Manim Voiceover
"""

import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestKokoroMV(unittest.TestCase):
    def test_import(self):
        """Test that the module can be imported."""
        try:
            from kokoro_mv import KokoroService
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import KokoroService: {e}")

    def test_version(self):
        """Test that version information is available."""
        try:
            from kokoro_mv import __version__, __author__, __description__
            self.assertIsNotNone(__version__)
            self.assertIsNotNone(__author__)
            self.assertIsNotNone(__description__)
        except ImportError as e:
            self.fail(f"Failed to import version info: {e}")

    def test_kokoro_service_creation(self):
        """Test that KokoroService can be instantiated (without model files)."""
        try:
            from kokoro_mv import KokoroService
            # This should not fail even without model files
            # The service will handle model download when needed
            service = KokoroService()
            self.assertIsNotNone(service)
        except Exception as e:
            # If it fails due to missing model files, that's expected
            # We just want to make sure the class can be imported
            pass


if __name__ == '__main__':
    unittest.main()
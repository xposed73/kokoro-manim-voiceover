# __init__.py

from .kokoro_service import KokoroService  # Import the KokoroService class
from .helper import remove_bookmarks, wav2mp3  # Import helper functions if needed

__all__ = ["KokoroService", "remove_bookmarks", "wav2mp3"]

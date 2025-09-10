# Kokoro Manim Voiceover

Professional library for generating high-quality voiceovers in Manim animations using the Kokoro-82M model.

[![Donate](https://raw.githubusercontent.com/nkayzai/kokoro-manim-voiceover/refs/heads/main/media/donation.png)](upi://pay?pa=nk73@upi)


## Installation

### From PyPI (Recommended)
```bash
pip install kokoro-manim-voiceover
```

### Using uv (Alternative)
```bash
# For new projects
uv init my-project
cd my-project
uv add kokoro-manim-voiceover

# Or install directly
uv pip install kokoro-manim-voiceover
```

**Note:** `uv` is a modern, high-performance Python package manager that offers significantly faster installations and better dependency resolution than pip. It's fully compatible with existing Python workflows.

### From Source
```bash
git clone https://github.com/nkayzai/kokoro-manim-voiceover.git
cd kokoro-manim-voiceover
pip install -e .
```

## Quick Start

```python
from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService

class MyAnimation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(voice="af"))
        
        with self.voiceover(text="Hello, this is my first voiceover!") as tracker:
            self.play(Write(Text("Hello, this is my first voiceover!")), run_time=tracker.duration)
```

## Available Voices

| Voice Code | Description |
|------------|-------------|
| `af` | American Female (default) |
| `af_bella` | American Female - Bella |
| `af_nicole` | American Female - Nicole |
| `af_sarah` | American Female - Sarah |
| `af_sky` | American Female - Sky |
| `am_adam` | American Male - Adam |
| `am_michael` | American Male - Michael |
| `bf_emma` | British Female - Emma |
| `bf_isabella` | British Female - Isabella |
| `bm_george` | British Male - George |
| `bm_lewis` | British Male - Lewis |

## Usage Examples

### Basic Animation
```python
class BasicExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(voice="af"))
        
        circle = Circle()
        square = Square().shift(2 * RIGHT)
        
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Now let's transform it into a square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)
```

### Custom Configuration
```python
service = KokoroService(
    voice="am_michael",  # Male voice
    speed=1.2,           # 20% faster
    lang="en-us"         # Language setting
)
```

## Requirements

- Python 3.11+
- Dependencies are automatically installed

## Model Files

The library automatically downloads required model files (~220MB) on first use.

## Development

### Setting up development environment

#### Using uv (Recommended)
```bash
# Clone the repository
git clone https://github.com/nkayzai/kokoro-manim-voiceover.git
cd kokoro-manim-voiceover

# Install in development mode with all dependencies
uv sync --dev

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .

# Type checking
uv run mypy .
```

#### Using pip
```bash
# Clone the repository
git clone https://github.com/nkayzai/kokoro-manim-voiceover.git
cd kokoro-manim-voiceover

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
isort .
```

## License


MIT License


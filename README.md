# Kokoro Manim Voiceover

[![PyPI version](https://badge.fury.io/py/kokoro-manim-voiceover.svg)](https://badge.fury.io/py/kokoro-manim-voiceover)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Professional library for generating high-quality voiceovers in Manim animations using the Kokoro-82M model.**

Transform your Manim animations with natural-sounding, synchronized voiceovers. Unlike other tools that are often paid or produce unnatural voice quality, Kokoro Manim Voiceover leverages the powerful **Kokoro-82M parameter model** to deliver high-quality, free, and lifelike voiceovers.

---

![Kokoro Manim Voiceover](https://raw.githubusercontent.com/xposed73/kokoro-manim-voiceover/refs/heads/main/banner.jpg)

## ✨ Features

- 🎤 **High-Quality TTS**: Powered by the Kokoro-82M model for natural-sounding voice
- 🎬 **Seamless Manim Integration**: Works perfectly with Manim animations
- 🚀 **Easy Installation**: Simple pip/uv installation with automatic model downloads
- 🎯 **Multiple Voices**: 12 different voice options to choose from
- 💾 **Smart Caching**: Automatic caching for improved performance
- 🔧 **Professional Setup**: Clean, maintainable codebase

## 🚀 Quick Start

### Installation

**Using pip:**
```bash
pip install kokoro-manim-voiceover
```

**Using uv:**
```bash
uv add kokoro-manim-voiceover
```

**From source (development):**
```bash
git clone https://github.com/xposed73/kokoro-manim-voiceover.git
cd kokoro-manim-voiceover
pip install -e .
```

### First Use

When you first use the library, you'll be prompted to download the model files (~220MB total). This is a one-time setup:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService

class MyAnimation(VoiceoverScene):
    def construct(self):
        # Model files will be downloaded automatically on first use
        self.set_speech_service(KokoroService(voice="af"))
        
        with self.voiceover(text="Hello, this is my first voiceover!") as tracker:
            self.play(Write(Text("Hello World!")), run_time=tracker.duration)
```

---

## 📋 Requirements

- **Python**: 3.11 or higher (3.12+ recommended)
- **Dependencies**: Automatically installed with the package
  - `kokoro-onnx>=0.3.6`
  - `manim>=0.19.0`
  - `manim-voiceover>=0.3.7`
  - `soundfile>=0.13.0`
  - `numpy>=1.21.0`
  - `scipy>=1.7.0`

---

## 🎤 Available Voices

Choose from 12 different voice options:

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

---

## 📖 Usage Examples

### Basic Animation with Voiceover

```python
from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService

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

### Advanced Configuration

```python
from kokoro_mv import KokoroService

# Custom configuration
service = KokoroService(
    voice="am_michael",  # Male voice
    speed=1.2,           # 20% faster
    lang="en-us"         # Language setting
)
```

### Multiple Voiceovers

```python
class MultiVoiceExample(VoiceoverScene):
    def construct(self):
        # Different voices for different speakers
        narrator = KokoroService(voice="af")
        character = KokoroService(voice="am_adam")
        
        self.set_speech_service(narrator)
        
        with self.voiceover(text="The narrator speaks first.") as tracker:
            self.play(Write(Text("Narrator")))
        
        # Switch to character voice
        self.set_speech_service(character)
        
        with self.voiceover(text="Then the character responds.") as tracker:
            self.play(Write(Text("Character")))
```

---

## 🔧 Model Files

The library automatically downloads the required model files on first use:

- **kokoro-v0_19.onnx** (~169MB) - Main TTS model
- **voices.bin** (~50MB) - Voice data

**Total download size**: ~220MB (one-time setup)

Files are cached locally and reused for future projects.

---

## 🛠️ Development Setup

For developers who want to contribute or modify the library:

```bash
# Clone the repository
git clone https://github.com/xposed73/kokoro-manim-voiceover.git
cd kokoro-manim-voiceover

# Install in development mode
python install.py

# Or manually:
pip install -e .
```

---

## 📚 API Reference

### KokoroService

```python
KokoroService(
    engine=None,           # Custom engine (optional)
    model_path="",         # Custom model path (optional)
    voices_path="",        # Custom voices path (optional)
    voice="af",            # Voice selection
    speed=1.0,             # Speech speed multiplier
    lang="en-us",          # Language code
    **kwargs               # Additional arguments
)
```

### Methods

- `generate_from_text(text, cache_dir=None, path=None)`: Generate audio from text
- `text_to_speech(text, output_file, voice_name, speed, lang)`: Direct TTS conversion

---

## 🎯 Running Examples

To run the included example:

```bash
# After installation
manim main.py KokoExample
```

Or create your own animation file and import the service:

```python
from kokoro_mv import KokoroService
```

---

## 🔧 Troubleshooting

### Model Download Issues

If model files fail to download automatically:

```bash
# Run the setup command manually
kokoro-mv-setup
```

### Common Issues

1. **Python Version**: Ensure you're using Python 3.11+
2. **Dependencies**: All dependencies are installed automatically
3. **Model Files**: ~220MB download required on first use
4. **Permissions**: Ensure write permissions in your project directory

### Getting Help

- 📖 Check the [documentation](https://github.com/xposed73/kokoro-manim-voiceover#readme)
- 🐛 Report issues on [GitHub Issues](https://github.com/xposed73/kokoro-manim-voiceover/issues)
- 💬 Join discussions in the [GitHub Discussions](https://github.com/xposed73/kokoro-manim-voiceover/discussions)

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)** - The core TTS engine
- **[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)** - The voice model
- **[Manim](https://github.com/ManimCommunity/manim)** - The animation engine
- **[Manim Voiceover](https://github.com/ManimCommunity/manim-voiceover)** - Voiceover integration

---

## 🌟 Support the Project

If you find this project helpful, consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code

Thank you for using Kokoro Manim Voiceover! 🎤✨


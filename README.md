# Kokoro Manim Voiceover Setup Guide

Discover **Kokoro Manim Voiceover**, a groundbreaking library for generating synchronized and realistic voiceovers in Manim animations. Unlike other tools, which are often either paid or produce unnatural voice quality, this library leverages the **Kokoro-82M parameter model** to deliver high-quality, free, and lifelike voiceovers. Follow the steps below to install and start using this innovative solution seamlessly.

---

![Kokoro Manim Voiceover](https://raw.githubusercontent.com/xposed73/kokoro-manim-voiceover/refs/heads/main/banner.jpg)

## 🔧 Installation via pip

### 1. Verify Your Python Version  
Ensure your Python version is **3.11** or higher (3.12+ recommended). Check your installed version using:  
```bash
python --version
```

### 2. Create a Virtual Environment  
It’s best to work in a virtual environment to isolate dependencies:  
```bash
python -m venv myenv
myenv\Scripts\activate  # Activate the environment on Windows
```

### 3. Install Kokoro Manim Voiceover  
Install the library directly from GitHub:  
```bash
pip install git+https://github.com/xposed73/kokoro-manim-voiceover.git
```

---

## 🚀 Installation via uv  
Alternatively, you can use **uv** for setup:  
```bash
uv init -p 3.11
uv venv
uv pip install git+https://github.com/xposed73/kokoro-manim-voiceover.git
```

---

## 🛠️ Easy Installation Script

For the easiest installation experience, use the provided installation script:

```bash
python install.py
```

This script will:
- ✅ Check your Python version compatibility
- ✅ Install all required dependencies
- ✅ Install the package in development mode
- ✅ Verify the installation works
- ⚠️  Remind you to download the required model files

---

### It will automatically install all the required things like manim, manim-voiceover etc.

## 📂 Important Notes  
- **Model files are automatically downloaded** when you first use KokoroService!
- The following files will be downloaded automatically if missing:
  - `kokoro-v0_19.onnx` (~169MB)
  - `voices.bin` (~50MB)
- Files are saved in your project directory for future use.

---

## 💡 Example Usage

Here's a sample script to demonstrate how to use Kokoro Manim Voiceover:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv.koko import KokoroService

class KokoExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(
            voice="af"  # Model files auto-downloaded if missing
        ))

        circle = Circle()
        square = Square().shift(2 * RIGHT)

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

        with self.voiceover(text="Now, let's transform it into a square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        self.wait()
```

---

## 🎤 Available Voice Names  
You can use any of the following voice options in your projects:  
`af`, `af_bella`, `af_nicole`, `af_sarah`, `af_sky`, `am_adam`, `am_michael`, `bf_emma`, `bf_isabella`, `bm_george`, `bm_lewis`

---

Enjoy creating seamless animations with synchronized voiceovers!

## Sources

- **[kokoro-onnx on GitHub](https://github.com/thewh1teagle/kokoro-onnx)**  
  Repository for the kokoro-onnx project, GitHub.

- **[Kokoro-82M on HuggingFace](https://huggingface.co/hexgrad/Kokoro-82M)**  
  Model repository for Kokoro-82M, HuggingFace.


## 🙏 Support My Work

If you find this project helpful, consider supporting it by donating via UPI.

![Donate via UPI](https://raw.githubusercontent.com/xposed73/YTDL-python/main/upi-donation.png)

Thank you for your support! ❤️


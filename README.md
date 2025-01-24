# Kokoro Manim Voiceover Setup Guide

Discover **Kokoro Manim Voiceover**, a groundbreaking library for generating synchronized and realistic voiceovers in Manim animations. Unlike other tools, which are often either paid or produce unnatural voice quality, this library leverages the **Kokoro-82M parameter model** to deliver high-quality, free, and lifelike voiceovers. Follow the steps below to install and start using this innovative solution seamlessly.

---

![Kokoro Manim Voiceover](https://raw.githubusercontent.com/xposed73/kokoro-manim-voiceover/refs/heads/main/kokoro-manim-voiceover.jpg)

## 🔧 Installation via pip

### 1. Verify Your Python Version  
Ensure your Python version is **3.12** (recommended). Check your installed version using:  
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
uv init -p 3.12
uv venv
uv pip install git+https://github.com/xposed73/kokoro-manim-voiceover.git
```

---

## 📂 Important Notes  
- You **must download the following model files** to enable voiceover functionality:
  - [`kokoro-v0_19.onnx`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx)
  - [`voices.bin`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin)
- Place these files in the **root directory** of your project.

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
            model_path="kokoro-v0_19.onnx",
            voices_path="voices.bin",
            voice="af"
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



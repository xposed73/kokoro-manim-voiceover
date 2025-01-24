# Kokoro Manim Voiceover

## Install via pip
Check python version (Recommended Python Version = 3.12)
```console
python --version
```

Create virtual environment
```console
python -m venv myenv
myenv\Scripts\activate
```

Install Kokoro-MV from github
```console
pip install git+https://github.com/xposed73/kokoro-manim-voiceover.git
```


## Install via uv
```console
uv init -p 3.12
uv venv
uv pip install git+https://github.com/xposed73/kokoro-manim-voiceover.git
```

## Important
- You also need to download these model files
[`kokoro-v0_19.onnx`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx) and [`voices.bin`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin)
- Place them in root directory of your project

## Example usage
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

## Available voice names
`af`, `af_bella`, `af_nicole`, `af_sarah`, `af_sky`, `am_adam`, `am_michael`, `bf_emma`, `bf_isabella`, `bm_george`, `bm_lewis`


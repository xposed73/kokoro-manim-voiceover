# Kokoro Manim Voiceover

Professional library for generating high-quality voiceovers in Manim animations using the Kokoro-82M model.

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
git clone https://github.com/xposed73/kokoro-manim-voiceover.git
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
        self.set_speech_service(KokoroService(voice="af_sarah", lang="en-us"))
        
        with self.voiceover(text="Hello, this is my first voiceover!") as tracker:
            self.play(Write(Text("Hello, this is my first voiceover!")), run_time=tracker.duration)
```

## Voices (Kokoro-82M)

This library uses the Kokoro-82M voice models. Below is a curated list of available voices grouped by language, adapted from the upstream model's VOICES.md.

Note: Voice quality varies by dataset size/quality. Some languages have fewer voices and may rely on fallback G2P. See the Kokoro-82M model card for details.

### English (American)
```
af_heart, af_alloy, af_aoede, af_bella, af_jessica, af_kore,
af_nicole, af_nova, af_river, af_sarah, af_sky,
am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael,
am_onyx, am_puck, am_santa
```

### English (British)
```
bf_alice, bf_emma, bf_isabella, bf_lily,
bm_daniel, bm_fable, bm_george, bm_lewis
```

### Japanese
```
jf_alpha, jf_gongitsune, jf_nezumi, jf_tebukuro,
jm_kumo
```

### Mandarin Chinese
```
zf_xiaobei, zf_xiaoni, zf_xiaoxiao, zf_xiaoyi,
zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang
```

### Spanish
```
ef_dora, em_alex, em_santa
```

### French
```
ff_siwis
```

### Hindi
```
hf_alpha, hf_beta, hm_omega, hm_psi
```

### Italian
```
if_sara, im_nicola
```

### Brazilian Portuguese
```
pf_dora, pm_alex, pm_santa
```

### Selecting voices and languages
- Set `voice` to one of the codes above.
- Set `lang` to match your target locale. Recommended codes for phonemizer compatibility:
  - English (US): `en-us`
  - English (GB): `en-gb`
  - Japanese: `ja`
  - Mandarin Chinese: `cmn` (instead of `zh`)
  - Spanish: `es`
  - French: `fr-fr` (instead of `fr`)
  - Hindi: `hi`
  - Italian: `it`
  - Brazilian Portuguese: `pt-br`

Example:
```python
self.set_speech_service(KokoroService(voice="hf_alpha", lang="hi"))
```

Source: Kokoro-82M VOICES.md by hexgrad (Apache-2.0).

## Video Samples

Preview recordings rendered from the included sample scenes:

**English (US)**
<video src="samples/english_us.mp4" width="560" controls></video>

**English (GB)**
<video src="samples/english_gb.mp4" width="560" controls></video>

**Hindi**
<video src="samples/hindi.mp4" width="560" controls></video>

**Mandarin Chinese**
<video src="samples/chinese_mandarian.mp4" width="560" controls></video>

**Spanish**
<video src="samples/spanish.mp4" width="560" controls></video>

**French**
<video src="samples/french.mp4" width="560" controls></video>

**Italian**
<video src="samples/italian.mp4" width="560" controls></video>

**Brazilian Portuguese**
<video src="samples/portuguese_br.mp4" width="560" controls></video>

## Sample Scenes (code)

Code examples for each language are available in the `samples/` folder. Each file sets an appropriate `voice` and `lang` and renders the same demo scene.

- `samples/english_us.py` → voice `af_sarah`, lang `en-us`
- `samples/english_gb.py` → voice `bf_emma`, lang `en-gb`
- `samples/hindi.py` → voice `hf_alpha`, lang `hi`
- `samples/chinese_mandarin.py` → voice `zf_xiaobei`, lang `cmn`
- `samples/spanish.py` → voice `ef_dora`, lang `es`
- `samples/french.py` → voice `ff_siwis`, lang `fr-fr`
- `samples/italian.py` → voice `if_sara`, lang `it`
- `samples/portuguese_br.py` → voice `pf_dora`, lang `pt-br`

Run any sample (replace the filename as needed):
```bash
# Option A: from repository root
manim -pql samples/english_us.py Example
# or with uv
uv run manim -pql samples/english_us.py Example

# Option B: cd into samples first
cd samples
manim -pql english_us.py Example
```

Notes:
- For Japanese and Mandarin, ensure eSpeak NG is installed and `lang` codes are set as above (e.g., `cmn` for Mandarin) to avoid phonemizer issues.
- If you encounter “phonemes too long” errors, split long narration into multiple `with self.voiceover(...)` blocks.
- The sample scenes use the `manim-dsa` library for data-structure visuals. Install it first if needed:
  ```bash
  pip install manim-dsa
  # OR
  uv add manim-dsa
  ```

## Usage Examples

### Basic Animation
```python
class BasicExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(voice="af_sarah", lang="en-us"))
        
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
    voice="af_sarah",    # Female voice
    speed=1.2,           # 20% faster
    lang="en-us",        # Language setting
    volume=1.2           # Volume
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
git clone https://github.com/xposed73/kokoro-manim-voiceover.git
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
git clone https://github.com/xposed73/kokoro-manim-voiceover.git
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


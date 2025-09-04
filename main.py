"""
Example usage of Kokoro Manim Voiceover
"""

from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv.koko import KokoroService


class KokoExample(VoiceoverScene):
    def construct(self):
        # Set up the Kokoro service (model files will be auto-downloaded if missing)
        self.set_speech_service(KokoroService(
            voice="af"  # You can change this to any available voice
        ))

        # Create some basic shapes
        circle = Circle()
        square = Square().shift(2 * RIGHT)

        # First voiceover with circle creation
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        # Second voiceover with movement
        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

        # Third voiceover with transformation
        with self.voiceover(text="Now, let's transform it into a square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        self.wait()


def main():
    print("Kokoro Manim Voiceover Example")
    print("=" * 40)
    print("This example demonstrates how to use KokoroService with Manim.")
    print("Model files will be automatically downloaded when needed!")
    print("\nTo run the animation, use:")
    print("manim main.py KokoExample")
    print("\nAvailable voices: af, af_bella, af_nicole, af_sarah, af_sky,")
    print("am_adam, am_michael, bf_emma, bf_isabella, bm_george, bm_lewis")


if __name__ == "__main__":
    main()

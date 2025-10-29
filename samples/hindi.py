from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # Hindi
        self.set_speech_service(KokoroService(voice="hf_alpha", lang="hi"))

        graph = {
            'A': [('C', 11), ('D', 7)],
            'B': [('A', 5),  ('C', 3)],
            'C': [('A', 11), ('B', 3)],
            'D': [('A', 7),  ('C', 4)],
        }

        nodes_and_positions = {
            'A': LEFT * 1.5,
            'B': UP * 2,
            'C': RIGHT * 1.5,
            'D': DOWN * 2,
        }

        mArray = (
            MArray([1, 2, 3], style=MArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=MStackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("Graph"))
            .to_edge(RIGHT, 1)
        )

        # Hindi narration
        with self.voiceover(text="बाईं तरफ हम तीन नंबरों वाला एक ऐरे बना रहे हैं और उसके इंडेक्स दिखा रहे हैं।") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="बीच में हम चार नंबरों वाला एक स्टैक बना रहे हैं।") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="दाईं तरफ हम चार नोड वाला एक ग्राफ बना रहे हैं।") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="इस सीन में ऐरे, स्टैक और ग्राफ को एक साथ दिखाया गया है।") as tracker:
            self.wait(tracker.duration)

from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # Use Hindi voice if supported
        self.set_speech_service(KokoroService(voice="hf_alpha", lang="hi"))

        graph = {
            'A': [('C', 11), ('D', 7)],
            'B': [('A', 5),  ('C', 3)],
            'C': [('A', 11), ('B', 3)],
            'D': [('A', 7),  ('C', 4)],
        }

        nodes_and_positions = {
            'A': LEFT * 1.5,
            'B': UP * 2,
            'C': RIGHT * 1.5,
            'D': DOWN * 2,
        }

        mArray = (
            MArray([1, 2, 3], style=MArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=MStackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("Graph"))
            .to_edge(RIGHT, 1)
        )

        # Simple, clear Hindi narration
        with self.voiceover(text="बाईं तरफ हम तीन नंबरों वाला एक ऐरे बना रहे हैं और उसके इंडेक्स दिखा रहे हैं।") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="बीच में हम चार नंबरों वाला एक स्टैक बना रहे हैं।") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="दाईं तरफ हम चार नोड वाला एक ग्राफ बना रहे हैं।") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="इस सीन में ऐरे, स्टैक और ग्राफ को एक साथ दिखाया गया है।") as tracker:
            self.wait(tracker.duration)
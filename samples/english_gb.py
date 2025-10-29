from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # English (GB)
        self.set_speech_service(KokoroService(voice="bf_emma", lang="en-gb"))

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

        # English (GB) narration
        with self.voiceover(text="On the left, we create an array of three numbers and show its indexes.") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="In the middle, we create a stack with four numbers.") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="On the right, we create a graph with four nodes.") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="This scene shows the array, stack, and graph together.") as tracker:
            self.wait(tracker.duration)



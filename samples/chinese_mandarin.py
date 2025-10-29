from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # Mandarin Chinese (use 'cmn' for eSpeak NG phonemizer compatibility)
        self.set_speech_service(KokoroService(voice="zf_xiaobei", lang="cmn"))

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
            .add_label(Text("数组"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=MStackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("栈"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("图"))
            .to_edge(RIGHT, 1)
        )

        # Chinese narration
        with self.voiceover(text="在左侧我们创建一个包含三个数字的数组，并显示它的索引。") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="在中间我们创建一个包含四个数字的栈。") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="在右侧我们创建一个有四个节点的图。") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="本场景同时展示数组、栈和图。") as tracker:
            self.wait(tracker.duration)



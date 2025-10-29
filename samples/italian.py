from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # Italian
        self.set_speech_service(KokoroService(voice="if_sara", lang="it"))

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
            .add_label(Text("Grafo"))
            .to_edge(RIGHT, 1)
        )

        # Italian narration
        with self.voiceover(text="A sinistra creiamo un array di tre numeri e ne mostriamo gli indici.") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="Al centro, creiamo uno stack con quattro numeri.") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="A destra, creiamo un grafo con quattro nodi.") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="Questa scena mostra insieme array, stack e grafo.") as tracker:
            self.wait(tracker.duration)



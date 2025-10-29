from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # Brazilian Portuguese
        self.set_speech_service(KokoroService(voice="pf_dora", lang="pt-br"))

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
            .add_label(Text("Pilha"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("Grafo"))
            .to_edge(RIGHT, 1)
        )

        # Portuguese (BR) narration
        with self.voiceover(text="À esquerda, criamos um array com três números e mostramos seus índices.") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="No meio, criamos uma pilha com quatro números.") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="À direita, criamos um grafo com quatro nós.") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="Esta cena mostra juntos o array, a pilha e o grafo.") as tracker:
            self.wait(tracker.duration)



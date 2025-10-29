from manim import *
from manim_dsa import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService


class Example(VoiceoverScene):
    def construct(self):
        # French (use 'fr-fr' for eSpeak NG phonemizer compatibility)
        self.set_speech_service(KokoroService(voice="ff_siwis", lang="fr-fr"))

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
            .add_label(Text("Tableau"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=MStackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Pile"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("Graphe"))
            .to_edge(RIGHT, 1)
        )

        # French narration
        with self.voiceover(text="À gauche, nous créons un tableau de trois nombres et affichons ses indices.") as tracker:
            self.play(Create(mArray), run_time=tracker.duration)

        with self.voiceover(text="Au centre, nous créons une pile avec quatre nombres.") as tracker:
            self.play(Create(mStack), run_time=tracker.duration)

        with self.voiceover(text="À droite, nous créons un graphe avec quatre nœuds.") as tracker:
            self.play(Create(mGraph), run_time=tracker.duration)

        with self.voiceover(text="Cette scène présente l’ensemble: tableau, pile et graphe.") as tracker:
            self.wait(tracker.duration)



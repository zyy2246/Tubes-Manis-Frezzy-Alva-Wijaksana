from manim import *

class AnimasiSederhana(Scene):
    def construct(self):
        # Ganti teks jadi "Selamat pagi"
        teks = Text("Selamat Sore", font_size=72)
        self.play(Write(teks))
        self.wait(1)

        self.play(teks.animate.shift(UP * 2))

        lingkaran = Circle(radius=1, color=BLUE)
        lingkaran.set_fill(BLUE, opacity=0.5)
        self.play(Create(lingkaran))
        self.wait(1)

        self.play(lingkaran.animate.shift(RIGHT * 3))
        self.play(lingkaran.animate.set_color(RED))
        self.wait(1)

        self.play(FadeOut(teks), FadeOut(lingkaran))
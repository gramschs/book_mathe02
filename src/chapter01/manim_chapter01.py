from manim import *

class FirstExample(Scene):
    def construct(self):

        ax = Axes(x_range=(-1,6,1), y_range=(-1,7, 1), 
                  tips=True,
                  axis_config={"include_numbers": True},)
        labels = ax.get_axis_labels(
             Tex("x").scale(0.7), Text("f(x)").scale(0.45)
        )
        curve = ax.plot(lambda x: x**2 -6*x +11, color=RED, x_range=[-0.5, 5.5])

        parallel_line = Line(start=ax.c2p(-1, 7), end=ax.c2p(6, 7), color=WHITE)

        self.add(ax, labels)
        self.play(Create(curve))
        self.add(parallel_line)
        self.play(parallel_line.animate.next_to(ax.c2p(-1, 2), ax.c2p(6,2), buff=0))

        # Hold the final frame
        self.wait()
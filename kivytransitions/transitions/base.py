from kivy.properties import StringProperty, ColorProperty, OptionProperty
from kivy.uix.screenmanager import ShaderTransition
from os import path

PATH = path.dirname(__file__)
EXTRA = path.join(PATH, "extra")


class CustomTransition(ShaderTransition):
    direction = OptionProperty("lr", options=["lr", "rl"])

    glsl_file = StringProperty("Bounce.glsl")

    clearcolor = ColorProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(path.join(EXTRA, "header.glsl")) as header, open(
            path.join(PATH, self.glsl_file)
        ) as glsl, open(path.join(EXTRA, "footer.glsl")) as footer:
            self.fs = header.read() + glsl.read() + footer.read()

    def add_screen(self, screen):
        super().add_screen(screen)
        self.render_ctx["resolution"] = list(map(float, screen.size))

        aspect_ratio = screen.size[0] / screen.size[1]

        if aspect_ratio >= 1:
            self.render_ctx["aspect"] = 1.0

        else:
            self.render_ctx["aspect"] = 2.0

        if self.direction == "lr":
            self.render_ctx["direction"] = 1.0

        else:
            self.render_ctx["direction"] = 2.0

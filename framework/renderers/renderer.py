from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from windows.window import Window
    from framework.scenes.scene import Scene

class Renderer:
    def __init__(self, window: "Window") -> None:
        self.window = window

    def fill(self, color: tuple[int, int, int]) -> None:
        self.window.pgwindow.get_surface().fill(color)

    def update(self) -> None:
        self.window.pgwindow.flip()

    def render_scene(self, scene: "Scene") -> None:
        for game_object in scene.contents.__dict__.values():
            game_object.components.__dict__["Image_Component"].render(self.window.pgwindow.get_surface())

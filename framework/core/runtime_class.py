
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.windows.window_manager import Window_Manager
    from framework.core.engine_class import Engine

class RunTime:
    """
    The RunTime class is responsible for managing the game loop and rendering the game scene.
    It initializes the game window, handles events, and updates the game state.
    """

    def __init__(self, winmanager: "Window_Manager", engine: "Engine", runtimefile: str) -> None:
        self.winmanager = winmanager

    def run(self):
        while True:
            for win in self.winmanager.get_all_windows().values():
                win.renderer.fill((0, 0, 0))
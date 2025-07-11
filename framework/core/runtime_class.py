
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.core.engine_class import Engine

class RunTime:
    """
    The RunTime class is responsible for managing the game loop and rendering the game scene.
    It initializes the game window, handles events, and updates the game state.
    """

    def __init__(self, engine: "Engine", runtimefile: str) -> None:
        self.engine = engine
        self.runtimefile = runtimefile
        
        self.sandbox = {}
        exec(open(self.runtimefile, "r").read(), self.sandbox)

    def run(self) -> None:
        while True:
            for win in self.engine.WINDOW_MANAGER.get_all_windows().values():
                win.renderer.fill((0, 0, 0))

                self.sandbox["logic"]()

            self.engine.EVENTS_HANDLER.handle_events(self.engine.WINDOW_MANAGER,
                                                    flags="WINDOWCLOSE | QUIT")


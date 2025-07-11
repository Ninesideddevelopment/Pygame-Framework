
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.core.engine_class import Engine

class StartUp:
    def __init__(self, engine: "Engine", startupfile: str) -> None:
        self.engine = engine
        self.startupfile = startupfile

    def initialize(self):
        """
        Initialize the game engine.
        This method should be called before starting the game loop.
        """
        with open(self.startupfile, "r+") as file:
            exec(file.read())
        print("Game engine initialized.")

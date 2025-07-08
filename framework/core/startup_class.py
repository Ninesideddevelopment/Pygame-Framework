
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.core.engine_class import Engine

class StartUp:
    def __init__(self, engine: "Engine", startupfile: str) -> None:
        self.engine = engine
        with open(startupfile, "a+") as file:
            exec(file.read())

    def initialize(self):
        """
        Initialize the game engine.
        This method should be called before starting the game loop.
        """
        # Perform any necessary setup here, such as loading resources, initializing subsystems, etc.
        print("Game engine initialized.")

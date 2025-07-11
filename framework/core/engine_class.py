from typing import TYPE_CHECKING

from framework.core.startup_class import StartUp
from framework.core.runtime_class import RunTime

if TYPE_CHECKING:
    from framework.windows.window_manager import Window_Manager
    from framework.core.events_handler import Events_Handler

class Engine:
    def __init__(self, startupfile: str, runtimefile: str) -> None:
        self.WINDOW_MANAGER: "Window_Manager"
        self.EVENTS_HANDLER: "Events_Handler"

        self.startup = StartUp(engine=self, startupfile=startupfile)
        self.runtime = RunTime(engine=self, runtimefile=runtimefile)

    def play(self):
        """
        Starts the game engine by initializing the startup process and running the runtime loop.
        """
        self.startup.initialize()
        self.runtime.run()

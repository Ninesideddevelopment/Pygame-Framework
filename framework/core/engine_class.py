from framework.core.startup_class import StartUp
from framework.core.runtime_class import RunTime

class Engine:
    def __init__(self, startupfile: str, runtimefile: str) -> None:
        self.startup = StartUp(engine=self, startupfile=startupfile)
        #self.runtime = RunTime(engine=self, runtimefile=runtimefile)

    def play(self):
        """
        Starts the game engine by initializing the startup process and running the runtime loop.
        """
        self.startup.initialize()
        #self.runtime.run()

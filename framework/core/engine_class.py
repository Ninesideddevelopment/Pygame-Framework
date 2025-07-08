from framework.core.startup_class import StartUp
from framework.core.runtime import RunTime

class Engine:
    def __init__(self) -> None:
        self.startup = StartUp(self)
        self.runtime = RunTime()
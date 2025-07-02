
from pygame import Window as WINDOW
from typing import Tuple

class Window:
    def __init__(self, title: str, size: Tuple[int, int], position: Tuple[int, int]) -> None:
        from framework.renderers.renderer import Renderer
        
        self.size = list(size)
        self.position = list(position)
        self.title = title
        
        self.renderer: Renderer = Renderer(window=self)
        
        # Create the pygame window with the specified title, size, and position
        self.pgwindow = WINDOW(title=self.title, size=self.size, position=self.position)
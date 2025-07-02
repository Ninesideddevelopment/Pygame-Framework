
from .default_container import DefaultContainer

class ComponentContainer(DefaultContainer):
    """A class created specifically to hold components for game objects, to avoid messy attributes."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
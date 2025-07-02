
from .default_container import DefaultContainer

class ObjectContainer(DefaultContainer):
    """A class created specifically to hold game objects for other classes, to avoid messy attributes."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
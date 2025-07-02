from typing import TYPE_CHECKING
from framework.windows.window import Window

if TYPE_CHECKING:
    from windows.window import Window

class Window_Manager:
    def __init__(self):
        from framework.containers.object_container import ObjectContainer
        self.windows = ObjectContainer()
    
    def add_window(self, window: 'Window') -> None:
        setattr(self.windows, window.title, window)
        
    def remove_window(self, title: str) -> None:
        if hasattr(self.windows, title):
            delattr(self.windows, title)
    
    def get_window(self, title: str) -> tuple[bool, Window | None]:
        return hasattr(self.windows, title), getattr(self.windows, title, None)
    
    def get_all_windows(self) -> dict[str, object]:
        return self.windows.__dict__
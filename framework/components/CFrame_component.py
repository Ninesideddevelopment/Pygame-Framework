
#Coordinates Frame Component - similar to the ones found in Roblox :D

from framework.components.default_component import Component
from pygame.math import Vector2

class CFrame_Component(Component):
    """A component that represents a CFrame, which is a coordinate frame with position, rotation, and size."""
    
    def __init__(self, position: Vector2, rotation: int, size: Vector2, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.position: Vector2 = position
        self.rotation: int = rotation
        self.size: Vector2 = size
        
    def set_position(self, position: Vector2) -> None:
        """Set the position of the CFrame.
        """
        self.position = position
        
    def set_rotation(self, rotation: int) -> None:
        """Set the rotation of the CFrame.
        """
        self.rotation = rotation
        
    def set_size(self, size: Vector2) -> None:
        """Set the size of the CFrame.
        """
        self.size = size
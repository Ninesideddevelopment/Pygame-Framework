
class Velocity_Component:
    """
    A component that manages the velocity of a game object.
    """
    
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y
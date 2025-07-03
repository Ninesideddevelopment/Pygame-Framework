
from .default_component import Component
import pygame

class Image_Component(Component):
    """A component that represents an image for a game object, which can be rendered on a surface."""
    
    def __init__(self, image_path: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        
        if self.image.get_alpha() is None:
            self.image = self.image.convert()
        else:
            self.image = self.image.convert_alpha()

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.game_object.components.CFrame_Component.x, self.game_object.components.CFrame_Component.y))
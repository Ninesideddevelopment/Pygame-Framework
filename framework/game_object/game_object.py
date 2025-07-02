
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.components.default_component import Component

class Game_Object:
    def __init__(self, components: list[Component] = []) -> None:
        from framework.containers.object_container import ObjectContainer
        
        self.components = ObjectContainer()
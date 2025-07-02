from framework.components import *

class Game_Object:
    def __init__(self, name: str, components: str = "") -> None:
        from framework.containers.object_container import ObjectContainer
        
        temp_components: list[str] = []
        current_component: str = ""
        for i in components:
            if i not in ["", " ", "|"]:
                current_component += i
            if i == "|":
                temp_components.append(current_component)
                current_component = ""
        
        self.name: str = name
        self.components = ObjectContainer()
        
        for component in temp_components:
            if component != "":
                self.components.__setattr__(component.__type__, component)
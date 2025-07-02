
class Scene:
    def __init__(self, name: str) -> None:
        from framework.containers.object_container import ObjectContainer
        
        self.name = name
        self.contents = ObjectContainer()
        
    def add_object(self, game_object):
        """Adds a game object to the scene."""
        self.contents.__setattr__(game_object.name, game_object)
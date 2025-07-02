
class Scene:
    def __init__(self, name: str) -> None:
        from framework.containers.object_container import ObjectContainer
        
        self.name = name
        self.contents = ObjectContainer()
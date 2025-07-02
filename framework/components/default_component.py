from framework.game_object.game_object import Game_Object

class Component:
    def __init__(self, game_object: Game_Object) -> None:
        self.game_object = game_object
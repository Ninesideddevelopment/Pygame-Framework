# pylint: skip-file

global engine
engine = self.engine

import pygame

from framework.windows.window_manager import Window_Manager
from framework.windows.window import Window
from framework.scenes.scene import Scene
from framework.core.events_handler import Events_Handler
from framework.game_object.game_object import Game_Object

engine.clock = pygame.time.Clock()

engine.WINDOW_MANAGER = Window_Manager()

engine.WINDOW_MANAGER.add_window(window = Window(title="Test_Window", size=(800, 600), position=(100, 100)))

engine.obj1 = Game_Object(name="Test_Object", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self) | Velocity_Component() |")
engine.obj2 = Game_Object(name="Test_Object2", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self, position=Vector2(200, 200)) |")

engine.scene = Scene("Scene 1")
engine.scene.add_object(engine.obj1)
engine.scene.add_object(engine.obj2)

engine.EVENTS_HANDLER = Events_Handler()
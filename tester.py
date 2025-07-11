from framework.windows.window import Window
from framework.windows.window_manager import Window_Manager
from framework.scenes.scene import Scene
from framework.core.events_handler import Events_Handler

from framework import *

import pygame
pygame.init()
from pygame.locals import *

from framework.game_object.game_object import Game_Object

clock = pygame.time.Clock()

winmanager = Window_Manager()

winmanager.add_window(window = Window(title="Test_Window", size=(800, 600), position=(100, 100)))

obj1 = Game_Object(name="Test_Object", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self) | Velocity_Component() |")
obj2 = Game_Object(name="Test_Object2", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self, position=Vector2(200, 200)) |")

scene = Scene("Scene 1")
scene.add_object(obj1)
scene.add_object(obj2)

ev_handler = Events_Handler()

while True:
    for win in winmanager.get_all_windows().values():
        win.renderer.fill((0, 0, 0))
    
    winmanager.get_window("Test_Window")[1].renderer.render_scene(scene)
    obj1.components.Velocity_Component.x += 0.25
    obj1.components.Velocity_Component.y += 0.25
    obj1.components.CFrame_Component.x += obj1.components.Velocity_Component.x
    obj1.components.CFrame_Component.y += obj1.components.Velocity_Component.y
    
    obj2.components.CFrame_Component.x += 1
        
    ev_handler.handle_events(winmanager, flags="WINDOWCLOSE | QUIT")
            
    for win in winmanager.get_all_windows().values():
        win.renderer.update()
        
    clock.tick(75)  # Limit to 75 FPS
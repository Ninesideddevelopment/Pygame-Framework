from framework.windows.window import Window
from framework.windows.window_manager import Window_Manager
from framework.core.scene import Scene

import pygame, sys
pygame.init()
from pygame.locals import *

from framework.game_object.game_object import Game_Object

from pygame.math import Vector2

clock = pygame.time.Clock()

winmanager = Window_Manager()

winmanager.add_window(window = Window(title="Test_Window", size=(800, 600), position=(100, 100)))

obj = Game_Object(name="Test_Object", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self) |")
obj2 = Game_Object(name="Test_Object2", components = "Image_Component(image_path='image.png', game_object=self) | CFrame_Component(game_object=self, position=Vector2(200, 200)) |")

scene = Scene("Scene 1")
scene.add_object(obj)
scene.add_object(obj2)

while True:
    for win in winmanager.get_all_windows().values():
        win.renderer.fill((0, 0, 0))
    
    winmanager.get_window("Test_Window")[1].renderer.render_scene(scene)
    obj.components.CFrame_Component.x += 1
    obj2.components.CFrame_Component.y += 1
        
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            winmanager.remove_window(title=event.window.title)
            event.window.destroy()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for win in winmanager.get_all_windows().values():
        win.renderer.update()
        
    clock.tick(75)  # Limit to 75 FPS
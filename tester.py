from framework.windows.window import Window
from framework.windows.window_manager import Window_Manager
from framework.core.scene import Scene

import pygame, sys
pygame.init()
from pygame.locals import *

winmanager = Window_Manager()

winmanager.add_window(window = Window(title="Test_Window", size=(800, 600), position=(100, 100)))

scene = Scene("Scene 1")

while True:
    print(winmanager.get_window("Test_Window")[1].renderer.draw_scene(scene))
        
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            winmanager.remove_window(title=event.window.title)
            event.window.destroy()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for win in winmanager.get_all_windows().values():
        win.renderer.fill((0, 0, 0))
        win.renderer.update()
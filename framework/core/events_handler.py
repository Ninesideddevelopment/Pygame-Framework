
from framework.underhood.flags_handler import return_flags
from framework.windows.window_manager import Window_Manager

import pygame, sys

class Events_Handler:
    def __init__(self) -> None:
        self.KeyCodes: dict("key", "value") = {}
    
    def handle_events(self, window_manager: Window_Manager, flags: str = "WINDOWCLOSE | QUIT") -> None:
        flags_list = return_flags(flags=flags)
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE and "WINDOWCLOSE" in flags_list:
                window_manager.remove_window(event.window.title)
                event.window.destroy()
            if event.type == pygame.QUIT and "QUIT" in flags_list:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.KeyCodes[event.key] = True
            if event.type == pygame.KEYUP:
                self.KeyCodes[event.key] = False
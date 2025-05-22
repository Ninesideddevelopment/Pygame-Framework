import pygame, math, numpy

class Tilemap:
    def __init__(self, imagepath:str):
        self.image = pygame.image.load(imagepath)

    def getPixel(self, coords:tuple):
        return self.image.get_at(coords)
    
    def getTile(self, coords_start:tuple, coords_end:tuple, colorkey:tuple=None):
        rect = pygame.Rect(coords_start[0], coords_start[1], coords_end[0]-coords_start[0], coords_end[1]-coords_start[1])
        tile = self.image.subsurface(rect)
        if colorkey != None:
            tile.set_colorkey(colorkey)
        return tile
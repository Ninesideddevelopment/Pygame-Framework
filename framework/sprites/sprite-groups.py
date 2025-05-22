import pygame

class SpriteGroup:
    def __init__(self):
        self.sprites = []

    def add(self, sprite):
        self.sprites.append(sprite)

    def remove(self, sprite):
        self.sprites.remove(sprite)
    
    def draw(self, surface, offset: tuple[int, int]):
        for sprite in self.sprites:
            if sprite.dirty:
                surface.blit(sprite.image, (sprite.rect.x - offset[0], sprite.rect.y - offset[1]))
                sprite.dirty = False

    def update_sprites(self):
        for sprite in self.sprites:
            sprite.update()
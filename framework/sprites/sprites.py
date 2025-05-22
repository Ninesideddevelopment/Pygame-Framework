import pygame

class Sprite:
    def __init__(self, image: pygame.Surface, start_position: tuple[int, int]):
        self.image = image
        self.rect = image.get_frect(topleft=start_position)
        self.dirty = False

        self.spriteAttr = {"gravity": 0,
                           "gravityMax": 10,
                           "gravityIncrease": 0.5,
                           "speed": 2,
                           }

        self.velocity = pygame.math.Vector2(0, 0)
        self.collision_types = {"top": False,
                                "bottom": False,
                                "right": False,
                                "left": False}
        
        self.movement = self.Movement(sprite=self)  
        self.collision = self.Collision(sprite=self)
    
    class Movement:
        def __init__(self, sprite):
            self.sprite = sprite

        def move(self, x:int, y:int):
            self.sprite.velocity.x += x
            self.sprite.velocity.y += y

        def moveto(self, position:tuple, x:bool, y:bool):
            if self.sprite.rect.x < position[0] and x:
                self.sprite.velocity.x += self.sprite.spriteAttr["speed"]
            elif self.sprite.rect.x > position[0] and x:
                self.sprite.velocity.x -= self.sprite.spriteAttr["speed"]
            else:
                self.sprite.velocity.x = 0

            if self.sprite.rect.y < position[1] and y:
                self.sprite.velocity.y += self.sprite.spriteAttr["speed"]
            elif self.sprite.rect.y > position[1] and y:
                self.sprite.velocity.y -= self.sprite.spriteAttr["speed"]
            else:
                self.sprite.velocity.y = 0

    class Collision:
        def __init__(self, sprite):
            self.sprite = sprite

            self.collisions = []

        def collide_rect_horizontal(self, rect):
            self.sprite.collision_types = {"top": False, "bottom": False, "right": False, "left": False}

            if self.sprite.velocity.x < 0:
                self.sprite.collision_types["left"] = True
                self.sprite.rect.left = rect.right
            if self.sprite.velocity.x > 0:
                self.sprite.collision_types["right"] = True
                self.sprite.rect.right = rect.left

        def collide_rect_vertical(self, rect):
            self.sprite.collision_types = {"top": False, "bottom": False, "right": False, "left": False}

            if self.sprite.velocity.y < 0:
                self.sprite.collision_types["top"] = True
                self.sprite.rect.top = rect.bottom
            if self.sprite.velocity.y > 0:
                self.sprite.collision_types["bottom"] = True
                self.sprite.rect.bottom = rect.top

        def collide_rects(self, allrects):
            self.sprite.collision_types = {"top": False, "bottom": False, "right": False, "left": False}

            self.sprite.rect.x += self.sprite.velocity.x
            self.collisions = [allrects[self.sprite.rect.collidelistall(allrects)[i]] for i in range(len(self.sprite.rect.collidelistall(allrects)))]
            for rect in self.collisions:
                self.collide_rect_horizontal(rect)

            self.sprite.rect.y += self.sprite.velocity.y
            self.collisions = [allrects[self.sprite.rect.collidelistall(allrects)[i]] for i in range(len(self.sprite.rect.collidelistall(allrects)))]
            for rect in self.collisions:
                self.collide_rect_vertical(rect)

    def update(self, allrects: list[pygame.Rect] = []):
        self.dirty = True
        self.velocity = pygame.math.Vector2(0, 0)
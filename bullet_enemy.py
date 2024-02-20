import pygame

clock = pygame.time.Clock()
pygame.init()
fire_up_enemy = False
fire_down_enemy = False


class BulEnemy(pygame.sprite.Sprite):
    def __init__(self, top, left):
        # Enemy bullet class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bomb2.png")
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def up_enemy(self):
        if fire_up_enemy:
            self.rect.top -= 10

    def down_enemy(self):
        if fire_down_enemy:
            self.rect.top += 20
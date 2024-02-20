import pygame

clock = pygame.time.Clock()
pygame.init()
fire_up = False
fire_down = False


class Bul(pygame.sprite.Sprite):
    def __init__(self, top, left):
        # Bullet class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bomb2.png")
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def up(self):
        if fire_up:
            self.rect.left = 40
            self.rect.top -= 10

    def down(self):
        if fire_down:
            self.rect.top += 10

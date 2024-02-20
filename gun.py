import pygame

pygame.init()


class Gun(pygame.sprite.Sprite):
    def __init__(self, screen, img):
        # Gun class
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.rect.left = 0
        self.rect.top = 510

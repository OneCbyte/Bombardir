import pygame.font


class Button:
    def __init__(self, screen, img, x, y):
        # Button class
        self.screen = screen
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)

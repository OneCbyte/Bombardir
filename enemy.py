import pygame
import random

pygame.init()

enemy_x = random.randint(300, 1000)
enemy_x_game = enemy_x // 25
enemy_x_game_win1 = enemy_x_game * 25 + 25 * 1
enemy_x_game_win2 = enemy_x_game * 25 + 25 * 2
enemy_x_game_win3 = enemy_x_game * 25 + 25 * 3


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Enemy class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/enemy.png")
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = enemy_x
        self.rect.top = 505

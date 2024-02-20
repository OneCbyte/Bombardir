import bullet_enemy
import cnarad
import enemy
import pygame
import pygame_gui
import random


class Settings:
    def __init__(self):
        # Game settings class
        self.settigs_color = (200, 200, 200)
        self.settigs_width = (1200)
        self.settigs_height = (800)
        self.settigs_bullet_en_left = random.randint(25, enemy.enemy_x)
        self.settigs_bullet_en_top = 520
        self.fps = 75
        self.bg_pozition = [0, 0]
        self.bg_image = pygame.image.load("img/fon.jpg")
        self.bg_menu = pygame.image.load("menu/fon.jpg")
        self.bg_skin = pygame.image.load("menu/fon.jpg")
        self.screen = pygame.display.set_mode((self.settigs_width, self.settigs_height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.sprite = pygame.sprite.Group()
        self.bullet_en = bullet_enemy.BulEnemy(self.settigs_bullet_en_top, 40 + enemy.enemy_x)
        self.manage = pygame_gui.UIManager((self.settigs_width, self.settigs_height))
        self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(525, 700, 100, 50),
                                                         manager=self.manage)
        self.enemy = enemy.Enemy()
        self.bullet = cnarad.Bul(520, 40)
        self.win = False
        self.second_life = False

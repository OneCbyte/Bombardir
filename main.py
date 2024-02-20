import bags
import bullet_enemy
import button
import cnarad
import enemy
import gun
import pygame
import pygame_gui
import random

import sys

from settings import Settings

# Initialize pygame and everything you need
pygame.init()
settings = Settings()
screen = settings.screen
pygame.display.set_caption("Bombardir")
clock = settings.clock

# We create everything necessary for the input field and configure it
manage = settings.manage
text_input = settings.input
text_input.set_allowed_characters('numbers')
text_input.set_text_length_limit(2)
text_input.set_text("0")

# Creating buttons for the menu
button_play = button.Button(screen, "menu/play.png", settings.screen_rect.centerx, 100)
button_skin = button.Button(screen, "menu/skin.png", settings.screen_rect.centerx, 250)
button_quit = button.Button(screen, "menu/exit.png", settings.screen_rect.centerx, 400)

# Creating buttons for the skins section
skin1 = button.Button(screen, "skins/skin1.png", 200, 400)
skin2 = button.Button(screen, "skins/skin2_2.png", 600, 400)
skin3 = button.Button(screen, "skins/skin3.png", 1000, 400)

# Setting up sprites
sprite = settings.sprite
bullet = settings.bullet
bullet_en = settings.bullet_en
Enemy = settings.enemy

# Flags for launching a specific part of the game
active_menu = True
active_game = False
active_skin = False
active_win = False
active_fail = False

# Loading the background
bg_menu = settings.bg_menu

# Load and play music in the background
pygame.mixer.music.load("sound/1-track-1.mp3")
pygame.mixer.music.play(-1, 0.0)
tab_button = pygame.mixer.Sound("sound/tab.mp3")
tab_button.set_volume(2)
win = pygame.mixer.Sound("sound/win.mp3")
fail = pygame.mixer.Sound("sound/fail.mp3")
shot = pygame.mixer.Sound("sound/shot.mp3")

# Creating icons for the victory and defeat menu
win_image = button.Button(screen, "img/win.png", settings.screen_rect.centerx, 450)
button_quit_win = button.Button(screen, "menu/exit.png", settings.screen_rect.centerx, 100)
fail_image = button.Button(screen, "img/fail.png", settings.screen_rect.centerx, 450)
button_quit_fail = button.Button(screen, "menu/exit.png", settings.screen_rect.centerx, 100)

while active_menu:
    # Launching the main menu
    pygame.mixer.music.pause()
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():
        # Listening to events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_play.rect.collidepoint(mouse_x, mouse_y):
                gun = gun.Gun(screen, "img/skin1.png")
                active_menu = False
                active_game = True
            if button_skin.rect.collidepoint(mouse_x, mouse_y):
                tab_button.play()
                active_menu = False
                active_skin = True
            if button_quit.rect.collidepoint(mouse_x, mouse_y):
                active_menu = False

    # Refresh the screen
    screen.blit(settings.bg_menu, settings.bg_pozition)
    button_play.draw()
    button_skin.draw()
    button_quit.draw()
    pygame.display.flip()

while active_skin:
    # Launch of a skin store
    pygame.mixer.music.pause()
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():
        # Listening to events
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if skin1.rect.collidepoint(mouse_x, mouse_y):
                gun = gun.Gun(screen, "img/skin1.png")
                active_skin = False
                active_game = True
            if skin2.rect.collidepoint(mouse_x, mouse_y):
                gun = gun.Gun(screen, "img/skin2.png")
                active_skin = False
                active_game = True
            if skin3.rect.collidepoint(mouse_x, mouse_y):
                gun = gun.Gun(screen, "img/skin3.png")
                active_skin = False
                active_game = True

    # Refresh the screen
    screen.blit(settings.bg_skin, settings.bg_pozition)
    skin1.draw()
    skin2.draw()
    skin3.draw()
    pygame.display.flip()

while active_game:
    # Starting the game
    pygame.mixer.music.unpause()
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                # Pressing the space bar
                bags.bags5.append(1)
                # Bug fix 5
                if len(bags.bags5) == 1:
                    shot.play()
                bags.bags2.append(1)

                # Bug fix 2
                if len(bags.bags2) > 1:
                    continue

                # Bug fix 1 and 3
                if len(bags.bags1) == 0:
                    bags.bags3.append(random.randint(3, 46))
                sprite.add(bullet)
                cnarad.fire_up = True
                bullet_en.rect.left = 40 + enemy.enemy_x
                bullet_en.rect.top = settings.settigs_bullet_en_top
                text_input.disable()
                bags.bags4.clear()

        elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element == text_input:
                # Input window
                text = text_input.get_text()

                if text == "":
                    bags.bags3.append(random.randint(3, 46))
                    break
                text_int = int(text)
                print(type(text_int))
                if text_int > 46 or text_int < 0:
                    bags.bags3.append(random.randint(3, 46))
                    break
                bags.bags3.append(text_int)
                bags.bags1.append(1)
        manage.process_events(event)

    # Refresh the screen
    manage.update(time_delta)
    screen.blit(settings.bg_image, settings.bg_pozition)
    manage.draw_ui(screen)
    sprite.add(Enemy, gun)
    bullet.up()
    bullet.down()
    bullet_en.up_enemy()
    bullet_en.down_enemy()
    sprite.draw(screen)
    pygame.display.flip()

    # Bullet tracking
    if bullet.rect.top == 0:
        cnarad.fire_up = False
        sprite.remove(bullet)
        bullet.rect.left = bags.bags3[-1] * 25
        sprite.add(bullet)
        cnarad.fire_down = True
    if bullet.rect.top == 560:
        cnarad.fire_down = False
        sprite.remove(bullet)
        # Win
        if bullet.rect.left == enemy.enemy_x_game_win1 or bullet.rect.left == enemy.enemy_x_game_win2 or \
                bullet.rect.left == enemy.enemy_x_game_win3:
            bags.bags4.append(1)
            active_game = False
            pygame.mixer.music.pause()
            pygame.mixer.music.load("sound/win.mp3")
            pygame.mixer.music.play(-1, 0.0)
            active_win = True
        sprite.add(bullet_en)
        bullet_enemy.fire_up_enemy = True

    if bullet_en.rect.top == 0:
        bullet_enemy.fire_up_enemy = False
        bullet_en.rect.left = random.randint(0, enemy.enemy_x)
        sprite.add(bullet_en)
        bullet_enemy.fire_down_enemy = True

    if bullet_en.rect.top == 560:
        bullet_enemy.fire_up_enemy = False
        bullet_enemy.fire_down_enemy = False
        # Defeat
        if bullet_en.rect.top >= 550 and bullet_en.rect.left <= 100:
            active_game = False
            pygame.mixer.music.pause()
            pygame.mixer.music.load("sound/fail.mp3")
            pygame.mixer.music.play(-1, 0.0)
            active_fail = True
        sprite.remove(bullet_en)
        bags.bags2.clear()
        bags.bags5.clear()
        text_input.enable()

    # Bug fix 4
    if bullet_enemy.fire_up_enemy:
        bags.bags4.append(1)
        if len(bags.bags4) == 1:
            shot.play()

# Victory Menu
while active_win:
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():
        # Listening to events
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_quit_win.rect.collidepoint(mouse_x, mouse_y):
                active_win = False

    screen.blit(settings.bg_skin, settings.bg_pozition)
    win_image.draw()
    button_quit_win.draw()
    pygame.display.flip()

# Defeat menu
while active_fail:
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():
        # Listening to events
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_quit_fail.rect.collidepoint(mouse_x, mouse_y):
                active_fail = False

    screen.blit(settings.bg_skin, settings.bg_pozition)
    fail_image.draw()
    button_quit_win.draw()
    pygame.display.flip()

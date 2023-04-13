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

pygame.init()
settings = Settings()
screen = settings.screen
manage = settings.manage
text_input = settings.input
text_input.set_allowed_characters('numbers')
text_input.set_text_length_limit(2)
text_input.set_text("0")
button_play = button.Button(screen, "menu/play.png", settings.screen_rect.centerx, 100)
button_skin = button.Button(screen, "menu/skin.png", settings.screen_rect.centerx, 250)
button_quit = button.Button(screen, "menu/exit.png", settings.screen_rect.centerx, 400)
skin1 = button.Button(screen, "skins/skin1.png", 200, 400)
skin2 = button.Button(screen, "skins/skin2_2.png", 600, 400)
skin3 = button.Button(screen, "skins/skin3.png", 1000, 400)
pygame.mixer.music.load("sound/1-track-1.mp3")
clock = settings.clock
sprite = settings.sprite
bullet = settings.bullet
bullet_en = settings.bullet_en

pygame.display.set_caption("Бомбардир")
pygame.mixer.music.play()
active_game = False
active_menu = True
active_skin = False
bg_menu = settings.bg_menu
Enemy = settings.enemy

while active_menu:
    time_delta = clock.tick(settings.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_play.rect.collidepoint(mouse_x, mouse_y):
                gun = gun.Gun(screen, "img/skin1.png")
                active_menu = False
                active_game = True
            if button_skin.rect.collidepoint(mouse_x, mouse_y):
                active_menu = False
                active_skin = True
            if button_quit.rect.collidepoint(mouse_x, mouse_y):
                active_menu = False

    screen.blit(settings.bg_menu, settings.bg_pozition)
    button_play.draw()
    button_skin.draw()
    button_quit.draw()
    pygame.display.flip()

while active_skin:
    time_delta = clock.tick(settings.fps)

    for event in pygame.event.get():
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

    screen.blit(settings.bg_skin, settings.bg_pozition)
    skin1.draw()
    skin2.draw()
    skin3.draw()
    pygame.display.flip()

while active_game:
    time_delta = clock.tick(settings.fps)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bags.bags2.append(1)
                if len(bags.bags2) > 1:
                    continue
                if len(bags.bags1) == 0:
                    bags.bags3.append(random.randint(3, 46))
                sprite.add(bullet)
                settings.shot.append(1)
                print(settings.lives)
                cnarad.fire_up = True
                bullet_en.rect.left = 40 + enemy.enemy_x
                bullet_en.rect.top = settings.settigs_bullet_en_top
                text_input.disable()
                if len(settings.shot) == 3:
                    settings.lives.append(1)
                    print("Активирован!")

        elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element == text_input:
                text = text_input.get_text()
                if text == "":
                    bags.bags3.append(random.randint(3, 46))
                    break
                text_int = int(text)
                if text_int > 46 or text_int < 0:
                    bags.bags3.append(random.randint(3, 46))
                    break
                bags.bags3.append(text_int)
                bags.bags1.append(1)

        manage.process_events(event)
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

    if len(settings.lives) == 0:
        print("Победа")
        active_game = False
    if bullet.rect.top == 0:
        cnarad.fire_up = False
        sprite.remove(bullet)
        bullet.rect.left = bags.bags3[-1] * 25
        sprite.add(bullet)
        cnarad.fire_down = True
    if bullet.rect.top == 560:
        cnarad.fire_down = False
        sprite.remove(bullet)
        sprite.add(bullet_en)
        bullet_enemy.fire_up_enemy = True
        if (bullet.rect.left == enemy.enemy_x_game_win1 or
                bullet.rect.left == enemy.enemy_x_game_win2 or
                bullet.rect.left == enemy.enemy_x_game_win3):
            settings.lives.pop(-1)

    if bullet_en.rect.top == 0:
        bullet_enemy.fire_up_enemy = False
        bullet_en.rect.left = random.randint(0, enemy.enemy_x)
        sprite.add(bullet_en)
        bullet_enemy.fire_down_enemy = True

    if bullet_en.rect.top == 560:
        bullet_enemy.fire_up_enemy = False
        bullet_enemy.fire_down_enemy = False
        if bullet_en.rect.top >= 550 and bullet_en.rect.left <= 100:
            sprite.remove(gun, bullet_en)
            print("Поражение!")
            active_game = False
        sprite.remove(bullet_en)
        bags.bags2.clear()
        text_input.enable()

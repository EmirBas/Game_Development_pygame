import pygame
import os
import random
from Tools import scenes
from Tools import handlers

pygame.mixer.init()

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

FPS = 60 

BONUS_VEL = 3 
STARTING_VEL = 5

BULLET_VEL = 8
BONUS_BULLETS = 2
STARTING_BULLETS = 3

MAX_HEALTH = 10
STARTING_HEALTH = 5

GEMI_WIDTH, GEMI_HEIGHT = 47, 40
IREM_HIT  = pygame.USEREVENT + 1
EMIR_HIT  = pygame.USEREVENT + 2

BONUS_HIT_EVENTS = {}
for i, item in enumerate(['ammo', 'hearth', 'speed']):
    BONUS_HIT_EVENTS[item]  = {}
    for j, player in enumerate(['left', 'right']):
        BONUS_HIT_EVENTS[item][player] = pygame.USEREVENT + 3 + i*2 +j

RANDOM_AMMO_LOC = []
RANDOM_HEARTH_LOC = []
RANDOM_SPEED_LOC = []

BONUS_TIMER_DICT = {}
for item in ['ammo', 'hearth', 'speed']:
    BONUS_TIMER_DICT[item]  = {}
    for player in ['left', 'right']:
        BONUS_TIMER_DICT[item][player] = None

ENABLED_BONUSES = ['ammo', 'hearth', 'speed']


def reset_stats():
    irem_stats , emir_stats = {}, {}
    irem_stats['movement_vel'] , emir_stats['movement_vel'] = STARTING_VEL, STARTING_VEL
    irem_stats['bullet_vel'] , emir_stats['bullet_vel'] = BULLET_VEL, BULLET_VEL
    irem_stats['bullet_cap'] , emir_stats['bullet_cap'] = STARTING_BULLETS, STARTING_BULLETS
    irem_stats['health'] , emir_stats['health'] = STARTING_HEALTH, STARTING_HEALTH
    irem_stats['bullets'] , emir_stats['bullets'] = [], []
    irem_stats['starting_x'], irem_stats['starting_y'] = 100, 300
    emir_stats['starting_x'], emir_stats['starting_y'] = 700, 300

    irem = pygame.Rect(irem_stats['starting_x'], irem_stats['starting_y'], GEMI_WIDTH, GEMI_HEIGHT)
    emir = pygame.Rect(emir_stats['starting_x'], emir_stats['starting_y'], GEMI_WIDTH, GEMI_HEIGHT)

    return irem_stats, emir_stats, irem, emir

def main():
    irem_stats, emir_stats, irem, emir = reset_stats()
    
    clock = pygame.time.Clock()
    run = True
    valid_window = 'opening'
    while run:
        clock.tick(FPS)
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if on_button == 'play':
                        valid_window = 'game'
                    if on_button == 'settings':
                        valid_window = 'settings'
                    if on_button == 'settings_back':
                        valid_window = 'opening'
                    if on_button == 'on_off_hearth':
                        if 'hearth' in ENABLED_BONUSES:
                            ENABLED_BONUSES.remove('hearth')
                        else:
                            ENABLED_BONUSES.append('hearth')
                    if on_button == 'on_off_ammo':
                        if 'ammo' in ENABLED_BONUSES:
                            ENABLED_BONUSES.remove('ammo')
                        else:
                            ENABLED_BONUSES.append('ammo')
                    if on_button == 'on_off_speed':
                        if 'speed' in ENABLED_BONUSES:
                            ENABLED_BONUSES.remove('speed')
                        else:
                            ENABLED_BONUSES.append('speed')
                    if on_button == 'winner_replay':
                        valid_window = 'opening'
                        irem_stats, emir_stats, irem, emir = reset_stats()

                    if on_button == 'winner_quit':
                        run = False
                        pygame.quit()

            if valid_window == 'game':            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(irem_stats['bullets']) < irem_stats['bullet_cap']:
                        bullet = pygame.Rect(irem.x + irem.width, irem.y + irem.height//2 -2, 10, 5)
                        irem_stats['bullets'].append(bullet)
                        BULLET_FIRE_SOUND.play()

                    if event.key == pygame.K_RCTRL and len(emir_stats['bullets']) < emir_stats['bullet_cap']:
                        bullet = pygame.Rect(emir.x - 10, emir.y + emir.height//2 -2, 10, 5)
                        emir_stats['bullets'].append(bullet)
                        BULLET_FIRE_SOUND.play()

                if event.type == IREM_HIT:
                    irem_stats['health'] -= 1
                    BULLET_HIT_SOUND.play()
                if event.type == EMIR_HIT:
                    emir_stats['health'] -= 1
                    BULLET_HIT_SOUND.play()

                for i, item in enumerate(['ammo', 'speed', 'hearth']):
                    for j, player in enumerate(['left', 'right']):
                        if event.type == BONUS_HIT_EVENTS[item][player]:
                            BONUS_TIMER_DICT[item][player]= pygame.time.get_ticks()
                            if item == 'ammo':
                                if player == 'left':
                                    irem_stats['bullet_cap'] += BONUS_BULLETS
                                elif player == 'right':
                                    emir_stats['bullet_cap'] += BONUS_BULLETS
                            if item == 'speed':
                                if player == 'left':
                                    irem_stats['movement_vel'] += BONUS_VEL
                                elif player == 'right':
                                    emir_stats['movement_vel'] += BONUS_VEL
                            if item == 'hearth':
                                if player == 'left' and irem_stats['health']<= 10:
                                    irem_stats['health'] += 1
                                elif player == 'right' and emir_stats['health']<= 10:
                                    emir_stats['health'] += 1



        if valid_window == 'game': 
            for item in ['ammo', 'speed']:
                for player in ['left', 'right']:
                    if BONUS_TIMER_DICT[item][player] is not None:
                        seconds = (pygame.time.get_ticks()-BONUS_TIMER_DICT[item][player])/1000
                        if seconds>5:
                            BONUS_TIMER_DICT[item][player] = None
                    if BONUS_TIMER_DICT[item][player] is None:
                        if item == 'ammo':
                            if player == 'left':
                                irem_stats['bullet_cap']  = STARTING_BULLETS
                            elif player == 'right':
                                emir_stats['bullet_cap']  = STARTING_BULLETS
                        if item == 'speed':
                            if player == 'left':
                                irem_stats['movement_vel']  = STARTING_VEL
                            elif player == 'right':
                                emir_stats['movement_vel']  = STARTING_VEL

            keys_pressed = pygame.key.get_pressed()
            irem = handlers.irem_handle_movement(keys_pressed, irem, irem_stats['movement_vel'])
            emir = handlers.emir_handle_movement(keys_pressed, emir, emir_stats['movement_vel'])
            irem_stats, emir_stats = handlers.handle_bullets(irem_stats, emir_stats, irem, emir, IREM_HIT, EMIR_HIT)
            handlers.bonus_object_collision(irem, emir, BONUS_HIT_EVENTS)

            if irem_stats['health'] <= 0 or emir_stats['health'] <= 0: 
                valid_window = 'winner'

        if valid_window == 'opening':
            on_button = scenes.opening_page(mouseX, mouseY)
        elif valid_window == 'settings':
            on_button = scenes.settings_page(mouseX, mouseY, ENABLED_BONUSES)
        elif valid_window == 'game':
            scenes.game_page(irem, emir, irem_stats['bullets'], emir_stats['bullets'], irem_stats['health'], emir_stats['health'], BONUS_TIMER_DICT, ENABLED_BONUSES)
        elif valid_window == 'winner':
            on_button = scenes.winner_page(irem_stats['health'], emir_stats['health'], mouseX, mouseY)
    main()

if __name__ == "__main__":
    main()

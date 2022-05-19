import pygame
from Tools import scenes

def irem_handle_movement(keys_pressed, irem, irem_vel):
    if keys_pressed[pygame.K_a] and irem.x - irem_vel > 0: # SOL
        irem.x -= irem_vel
    if keys_pressed[pygame.K_d] and irem.x + irem.width + irem_vel < scenes.get_width()/2 - scenes.get_border_thickness()/2: # SAĞ
        irem.x += irem_vel
    if keys_pressed[pygame.K_s] and irem.y + irem.height + irem_vel < scenes.get_height(): # ALT
        irem.y += irem_vel            # + çünkü sol üst 0,0 yukarı çıkmak için y azalmalı
    if keys_pressed[pygame.K_w] and irem.y - irem_vel > 0: # ÜST
        irem.y -= irem_vel
    return irem


def emir_handle_movement(keys_pressed, emir, emir_vel):
    if keys_pressed[pygame.K_LEFT] and emir.x - emir_vel > scenes.get_width()/2 + scenes.get_border_thickness()/2: # SOL
        emir.x -= emir_vel
    if keys_pressed[pygame.K_RIGHT] and emir.x + emir.width + emir_vel < scenes.get_width(): # SAĞ
        emir.x += emir_vel
    if keys_pressed[pygame.K_DOWN] and emir.y + emir.height + emir_vel < scenes.get_height(): # ALT
        emir.y += emir_vel            # + çünkü sol üst 0,0 yukarı çıkmak için y azalmalı
    if keys_pressed[pygame.K_UP] and emir.y - emir_vel > 0: # ÜST
        emir.y -= emir_vel
    return emir


def handle_bullets(irem_stats, emir_stats, irem, emir, IREM_HIT, EMIR_HIT):
    for bullet in irem_stats['bullets']:
        bullet.x += irem_stats['bullet_vel']
        if emir.colliderect(bullet):
            pygame.event.post(pygame.event.Event(EMIR_HIT))
            irem_stats['bullets'].remove(bullet)
        if bullet.x > scenes.get_width():
            irem_stats['bullets'].remove(bullet)

    for bullet in emir_stats['bullets']:
        bullet.x -= emir_stats['bullet_vel']
        if irem.colliderect(bullet):
            pygame.event.post(pygame.event.Event(IREM_HIT))
            emir_stats['bullets'].remove(bullet)
        if bullet.x < 0:
            emir_stats['bullets'].remove(bullet)
    
    return irem_stats, emir_stats


def bonus_object_collision(irem, emir, hit_events):
    for item in ['ammo', 'speed', 'hearth']:
        bonus_width , bonus_height = scenes.get_bonus_object_shape(item)
        bonus_loc_x, bonus_loc_y = scenes.get_bonus_object_loc(item)
        bonus_rect = pygame.Rect(bonus_loc_x, bonus_loc_y, bonus_width, bonus_height)
        if emir.colliderect(bonus_rect):
            player = 'right'
            pygame.event.post(pygame.event.Event(hit_events[item][player]))
            scenes.delete_bonus_object(item)
        elif irem.colliderect(bonus_rect):
            player = 'left'
            pygame.event.post(pygame.event.Event(hit_events[item][player]))
            scenes.delete_bonus_object(item)
            
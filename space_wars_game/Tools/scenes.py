import pygame
import os
import random
from pathlib import Path
from Tools import handlers
pygame.font.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I love İrem")

# COLORS
WHITE = (255, 255, 255)
RED  = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW= (255, 255, 0)
MAGENTA= (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# OPENING PAGE
OPENING_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'open_page.jpg')), (WIDTH, HEIGHT))
WARSHIP1 = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'warship1.png')), (300, 160))
WARSHIP2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'warship2.png')), (300, 160)), 310)
RED_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'red_button.png')), (250, 60))

# SETTINGS PAGE
SETTINGS_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'settings_background.jpg')), (WIDTH, HEIGHT))
BLANK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'grey_button.png')), (220, 40))
ENABLED_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'on-button.png')), (45, 35))
DISABLED_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'off-button.png')), (45, 35))
SETTING_BACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'back.png')), (100, 100))

# GAME PAGE
SPACE  = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space5.png')), (WIDTH, HEIGHT))
HEARTH = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'hearth.png')), (30, 30))

GEMI_WIDTH, GEMI_HEIGHT = 47, 40
IREMIN_GEMISI_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
IREMIN_GEMISI = pygame.transform.rotate(pygame.transform.scale(IREMIN_GEMISI_IMAGE, (GEMI_WIDTH, GEMI_HEIGHT)), 90)
EMIRIN_GEMISI_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
EMIRIN_GEMISI = pygame.transform.rotate(pygame.transform.scale(EMIRIN_GEMISI_IMAGE, (GEMI_WIDTH, GEMI_HEIGHT)), 270)

BORDER_THCIKNESS = 20
BORDER_BRICK = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'wall.png')), (BORDER_THCIKNESS, BORDER_THCIKNESS)), 90)

# WINNER PAGE
WIN_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'win_screen.jpg')), (WIDTH, HEIGHT))
WINNER_FONT = pygame.font.SysFont('comicsans', 70)
REPLAY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'replay.png')), (60, 60))
QUIT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'quit.png')), (60, 60))


# BONUS OBJECTS
AMMO_LOC = [WIDTH, HEIGHT]
SPEED_LOC = [WIDTH, HEIGHT]
HEARTH_LOC = [WIDTH, HEIGHT]

BONUS_AMMO = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'ammo.png')), (25, 25))
BONUS_SPEED = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'speed.png')), (25, 25))
BONUS_HEARTH = pygame.transform.scale(pygame.image.load(os.path.join(Path(__file__).parent.parent, 'Assets', 'hearth_bonus.png')), (25, 25))

def get_width():
    return WIDTH

def get_height():
    return HEIGHT

def get_border_thickness():
    return BORDER_THCIKNESS

def get_bonus_object_shape(bonus_name):
    if bonus_name == 'ammo':
        return BONUS_AMMO.get_width(), BONUS_AMMO.get_height()
    if bonus_name == 'speed':
        return BONUS_SPEED.get_width(), BONUS_SPEED.get_height()
    if bonus_name == 'hearth':
        return BONUS_HEARTH.get_width(), BONUS_HEARTH.get_height()

def get_bonus_object_loc(bonus_name):
    if bonus_name == 'ammo':
        return AMMO_LOC[0], AMMO_LOC[1]
    if bonus_name == 'speed':
        return SPEED_LOC[0], SPEED_LOC[1]
    if bonus_name == 'hearth':
        return HEARTH_LOC[0], HEARTH_LOC[1]

def create_bonus_objects(enabled_bonuses):
    global AMMO_LOC, SPEED_LOC, HEARTH_LOC
    rand = random.random()
    if 'ammo' in enabled_bonuses:
        if rand < 0.001 and AMMO_LOC[1] >= HEIGHT:
            rand_loc_x = random.random() * (WIDTH - BONUS_AMMO.get_width())
            rand_loc_y = -BONUS_AMMO.get_height()
            AMMO_LOC = [rand_loc_x, rand_loc_y]
        else:
            AMMO_LOC[1] +=  4

    if 'speed' in enabled_bonuses:
        if (rand >= 0.001 and rand < 0.002) and SPEED_LOC[1] >= HEIGHT:
            rand_loc_x = random.random() * (WIDTH - BONUS_SPEED.get_width())
            rand_loc_y = -BONUS_SPEED.get_height()
            SPEED_LOC = [rand_loc_x, rand_loc_y]
        else:
            SPEED_LOC[1] +=  4

    if 'hearth' in enabled_bonuses:
        if (rand >= 0.002 and rand < 0.003) and HEARTH_LOC[1] >= HEIGHT:
            rand_loc_x = random.random() * (WIDTH - BONUS_HEARTH.get_width())
            rand_loc_y = -BONUS_HEARTH.get_height()
            HEARTH_LOC = [rand_loc_x, rand_loc_y]
        else:
            HEARTH_LOC[1] +=  4
       
def draw_bonus_objects():
    if not AMMO_LOC[1] >= HEIGHT:
        WIN.blit(BONUS_AMMO, (AMMO_LOC[0], AMMO_LOC[1]))
    if not SPEED_LOC[1] >= HEIGHT:
        WIN.blit(BONUS_SPEED, (SPEED_LOC[0], SPEED_LOC[1]))
    if not HEARTH_LOC[1] >= HEIGHT:
        WIN.blit(BONUS_HEARTH, (HEARTH_LOC[0], HEARTH_LOC[1]))

def delete_bonus_object(bonus_name):
    global AMMO_LOC, SPEED_LOC, HEARTH_LOC
    if bonus_name == 'ammo':
        AMMO_LOC = [WIDTH, HEIGHT]
    if bonus_name == 'speed':
        SPEED_LOC = [WIDTH, HEIGHT]
    if bonus_name == 'hearth':
        HEARTH_LOC = [WIDTH, HEIGHT]

# MAIN PAGE FUNCTIONS
def opening_page(mouseX, mouseY):
    on_button = None
    configs = {}
    #pth = os.path.join(Path(__file__).parent.parent, 'Assets', 'irm1.png')

    # BACKGROUND
    configs['background'] = {}
    configs['background']['value'] = OPENING_BACKGROUND
    configs['background']['loc'] = (0,0)

    # SPACESHIPS
    configs['warship1'] = {}
    configs['warship1']['value'] = WARSHIP1
    configs['warship1']['loc'] = (20,20)

    configs['warship2'] = {}
    configs['warship2']['value'] = WARSHIP2
    configs['warship2']['loc'] = (WIDTH - WARSHIP2.get_width() - 20, HEIGHT - WARSHIP2.get_height() -20)

    # PLAY BUTTON
    configs['play_button'] = {}
    play_button = RED_BUTTON
    play_button_loc = (WIDTH/2 - play_button.get_width()/2, HEIGHT/2 - play_button.get_height()/2)
    if mouseX > play_button_loc[0] and mouseX < play_button_loc[0] + play_button.get_width():
        if mouseY > play_button_loc[1] and mouseY < play_button_loc[1] + play_button.get_height():
            on_button = 'play'
            play_button = pygame.transform.scale(play_button, (250*1.1, 60*1.1))
            play_button_loc = (WIDTH/2 - play_button.get_width()/2, HEIGHT/2 - play_button.get_height()/2)
    configs['play_button']['value'] = play_button
    configs['play_button']['loc'] = play_button_loc

    configs['play_text'] = {}
    play_text = pygame.font.SysFont('lucidasans', 20, bold = True).render('Play' , 1, WHITE)
    configs['play_text']['value'] = play_text
    configs['play_text']['loc'] = (WIDTH/2 - play_text.get_width()/2, HEIGHT/2 +5 - play_text.get_height()/2)

    # SETTINGS BUTTON
    configs['settings_button'] = {}
    settings_button = RED_BUTTON
    settings_button_loc = (WIDTH/2 - settings_button.get_width()/2, HEIGHT/2 - settings_button.get_height()/2 + 60)
    if mouseX > settings_button_loc[0] and mouseX < settings_button_loc[0] + settings_button.get_width():
        if mouseY > settings_button_loc[1] and mouseY < settings_button_loc[1] + settings_button.get_height():
            on_button = 'settings'
            settings_button = pygame.transform.scale(settings_button, (250*1.1, 60*1.1))
            settings_button_loc = (WIDTH/2 - settings_button.get_width()/2, HEIGHT/2 - settings_button.get_height()/2 + 60)
    configs['settings_button']['value'] = settings_button
    configs['settings_button']['loc'] = settings_button_loc
    configs['settings_text'] = {}
    settings_text = pygame.font.SysFont('lucidasans', 20, bold = True).render('Settings' , 1, WHITE)
    configs['settings_text']['value'] = settings_text
    configs['settings_text']['loc'] = (WIDTH/2 - settings_text.get_width()/2, HEIGHT/2 +5 - settings_text.get_height()/2+ 60)

    for key in configs.keys():
        WIN.blit(configs[key]['value'], configs[key]['loc'])
    pygame.display.update() 
    return on_button

    
def settings_page(mouseX, mouseY, enabled_list):
    on_button = None
    configs = {}
    
    # BACKGROUND
    configs['background'] = {}
    configs['background']['value'] = SETTINGS_BACKGROUND
    configs['background']['loc'] = (0,0)

    # SETTINGS 
    configs['settings_text'] = {}
    settings_text = pygame.font.SysFont('comicsans', 60).render('SETTINGS' , 1, BLUE)
    configs['settings_text']['value'] = settings_text
    configs['settings_text']['loc'] = (50, 20)


    # HEART BONUS SETTING
    configs['blank_hearth_button'] = {}
    configs['blank_hearth_button']['value'] = BLANK_BUTTON
    configs['blank_hearth_button']['loc'] = (85, 197)

    configs['hearth_text'] = {}
    hearth_text = pygame.font.SysFont('comicsans', 20).render('Bonus Hearths' , 1, BLACK)
    configs['hearth_text']['value'] = hearth_text
    configs['hearth_text']['loc'] = (100, 200)
    
    configs['hearth_button'] = {}
    if 'hearth' in enabled_list:
        the_button = ENABLED_BUTTON
    else:
        the_button = DISABLED_BUTTON
    configs['hearth_button']['value'] = the_button
    configs['hearth_button']['loc'] = (250, 200)

    if mouseX > configs['hearth_button']['loc'][0] and mouseX < configs['hearth_button']['loc'][0] + the_button.get_width():
        if mouseY > configs['hearth_button']['loc'][1] and mouseY < configs['hearth_button']['loc'][1] + the_button.get_height():
            on_button = 'on_off_hearth'


    # AMMO BONUS SETTING
    configs['blank_ammo_button'] = {}
    configs['blank_ammo_button']['value'] = BLANK_BUTTON
    configs['blank_ammo_button']['loc'] = (85, 247)

    configs['ammo_booster'] = {}
    ammo_booster = pygame.font.SysFont('comicsans', 20).render('Ammo Booster' , 1, BLACK)
    configs['ammo_booster']['value'] = ammo_booster
    configs['ammo_booster']['loc'] = (100, 250)

    configs['ammo_button'] = {}
    if 'ammo' in enabled_list:
        the_button = ENABLED_BUTTON
    else:
        the_button = DISABLED_BUTTON
    configs['ammo_button']['value'] = the_button
    configs['ammo_button']['loc'] = (250, 250)

    if mouseX > configs['ammo_button']['loc'][0] and mouseX < configs['ammo_button']['loc'][0] + the_button.get_width():
        if mouseY > configs['ammo_button']['loc'][1] and mouseY < configs['ammo_button']['loc'][1] + the_button.get_height():
            on_button = 'on_off_ammo'

    # SPEED BONUS SETTING
    configs['blank_speed_button'] = {}
    configs['blank_speed_button']['value'] = BLANK_BUTTON
    configs['blank_speed_button']['loc'] = (85, 297)

    configs['speed_booster'] = {}
    speed_booster = pygame.font.SysFont('comicsans', 20).render('Speed Booster' , 1, BLACK)
    configs['speed_booster']['value'] = speed_booster
    configs['speed_booster']['loc'] = (100, 300)

    configs['speed_button'] = {}
    if 'speed' in enabled_list:
        the_button = ENABLED_BUTTON
    else:
        the_button = DISABLED_BUTTON
    configs['speed_button']['value'] = the_button
    configs['speed_button']['loc'] = (250, 300)

    if mouseX > configs['speed_button']['loc'][0] and mouseX < configs['speed_button']['loc'][0] + the_button.get_width():
        if mouseY > configs['speed_button']['loc'][1] and mouseY < configs['speed_button']['loc'][1] + the_button.get_height():
            on_button = 'on_off_speed'


    # BACK BUTTON
    configs['back_button'] = {}
    back_button = SETTING_BACK_BUTTON
    back_button_loc = (WIDTH - back_button.get_width() -20, HEIGHT - back_button.get_height() -20)
    if mouseX > back_button_loc[0] and mouseX < back_button_loc[0] + back_button.get_width():
        if mouseY > back_button_loc[1] and mouseY < back_button_loc[1] + back_button.get_height():
            on_button = 'settings_back'
            back_button = pygame.transform.scale(back_button, (100*1.1, 100*1.1))
            back_button_loc = (WIDTH - back_button.get_width() -20, HEIGHT - back_button.get_height() -20)
    configs['back_button']['value'] = back_button
    configs['back_button']['loc'] = back_button_loc


    for key in configs.keys():
        WIN.blit(configs[key]['value'], configs[key]['loc'])
    pygame.display.update() 
    return on_button


def game_page(irem, emir, irem_bullets, emir_bullets, irem_health, emir_health, bonus_timer_dict, enabled_bonuses):
    WIN.blit(SPACE, (0,0)) 
    
    for i in range(HEIGHT//20+1):
        WIN.blit(BORDER_BRICK, (WIDTH//2-BORDER_THCIKNESS/2 -2, i*BORDER_THCIKNESS))

    for i in range(irem_health):
        WIN.blit(HEARTH, (10 + i*25,10))

    for i in range(emir_health):
        WIN.blit(HEARTH, (WIDTH - i*25 - 35,10))

    WIN.blit(IREMIN_GEMISI, (irem.x, irem.y))
    WIN.blit(EMIRIN_GEMISI, (emir.x, emir.y))

    for bullet in irem_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in emir_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for item in ['ammo', 'speed']:
        for player in ['left', 'right']:
            if bonus_timer_dict[item][player] is not None:
                time_left = 5- (pygame.time.get_ticks()-bonus_timer_dict[item][player])/1000
                timer = pygame.font.SysFont('comicsans', 15, bold= True).render(f'{time_left:.2f}' , 1,  RED)
                if item == 'ammo':
                    if player == 'left':
                        WIN.blit(BONUS_AMMO, (15, 40))
                        WIN.blit(timer, (50, 40))
                    if player == 'right':
                        WIN.blit(BONUS_AMMO, (WIDTH- BONUS_AMMO.get_width() - 15, 40))
                        WIN.blit(timer, (WIDTH - 85, 40))
                if item == 'speed':
                    if player == 'left':
                        WIN.blit(BONUS_SPEED, (15, 70))
                        WIN.blit(timer, (50, 70))
                    if player == 'right':
                        WIN.blit(BONUS_SPEED, (WIDTH- BONUS_SPEED.get_width() - 15, 70))
                        WIN.blit(timer, (WIDTH - 85, 70))
    create_bonus_objects(enabled_bonuses)
    draw_bonus_objects()
    pygame.display.update() 


def winner_page(irem_health, emir_health, mouseX, mouseY):
    on_button = None
    configs = {}

    # BACKGROUND
    configs['background'] = {}
    configs['background']['value'] = WIN_BACKGROUND
    configs['background']['loc'] = (0,0)


    # WINNER TEXT
    configs['winner_text'] = {}
    if irem_health <= 0 and emir_health <= 0: 
        winner_text = 'WHAT A DRAW!!!'
    elif irem_health <= 0: 
        winner_text = 'İREMİM KAZANDI'
    elif emir_health <= 0: 
        winner_text = 'EMİR KAZANDI'
    
    draw_text_winner = WINNER_FONT.render(winner_text, 1, WHITE)
    configs['winner_text']['value'] = draw_text_winner
    configs['winner_text']['loc'] = (WIDTH//2- draw_text_winner.get_width()//2, HEIGHT//2 - draw_text_winner.get_height()//2)

    # REPLAY BUTTON
    configs['replay_button'] = {}
    replay_button = REPLAY_BUTTON
    replay_button_loc = (WIDTH/2 - replay_button.get_width() -30, HEIGHT/2 + replay_button.get_height() + 20)
    if mouseX > replay_button_loc[0] and mouseX < replay_button_loc[0] + replay_button.get_width():
        if mouseY > replay_button_loc[1] and mouseY < replay_button_loc[1] + replay_button.get_height():
            on_button = 'winner_replay'
            replay_button = pygame.transform.scale(replay_button, (replay_button.get_width()*1.1, replay_button.get_height()*1.1))
            replay_button_loc = (WIDTH/2 - replay_button.get_width() -30, HEIGHT/2 + replay_button.get_height() + 20)
    configs['replay_button']['value'] = replay_button
    configs['replay_button']['loc'] = replay_button_loc


    # REPLAY BUTTON
    configs['quit_button'] = {}
    quit_button = QUIT_BUTTON
    quit_button_loc = (WIDTH/2 + 30, HEIGHT/2 + quit_button.get_height() + 20)
    if mouseX > quit_button_loc[0] and mouseX < quit_button_loc[0] + quit_button.get_width():
        if mouseY > quit_button_loc[1] and mouseY < quit_button_loc[1] + quit_button.get_height():
            on_button = 'winner_quit'
            quit_button = pygame.transform.scale(quit_button, (quit_button.get_width()*1.1, quit_button.get_height()*1.1))
            quit_button_loc = (WIDTH/2 + 30, HEIGHT/2 + quit_button.get_height() + 20)
    configs['quit_button']['value'] = quit_button
    configs['quit_button']['loc'] = quit_button_loc

    for key in configs.keys():
        WIN.blit(configs[key]['value'], configs[key]['loc'])
    pygame.display.update()

    return on_button

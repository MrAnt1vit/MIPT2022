# Imports
import pygame
from pygame.locals import *
from colors import *
from draw import update_screen
from consts import SIZE, TITLE, FPS, v_man

# Initialize game engine
pygame.init()

# Window
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

# Config
lights_on = True
day = True
man = [300, 400]

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                lights_on = not lights_on
            elif event.key == pygame.K_e:
                day = not day
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        man[-1] = max(man[-1] - v_man / FPS, 120)
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        man[-1] = min(man[-1] + v_man / FPS, 470)
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        man[0] = max(man[0] - v_man / FPS, 115)
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        man[0] = min(man[0] + v_man / FPS, 650)

    # Game logic
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN

    update_screen(screen, light_color, sky_color, field_color, stripe_color, day, lights_on, DARKNESS, man)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
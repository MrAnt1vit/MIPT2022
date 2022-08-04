from consts import *
import pygame


def update_screen(screen, light_color, sky_color, field_color, stripe_color, day, lights_on, DARKNESS, man):
    screen.fill(sky_color)

    # stripes
    pygame.draw.rect(screen, field_color, [0, 180, 800, 420])
    for i in coords_stripes:
        pygame.draw.rect(screen, stripe_color, i)

    # sun
    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40])
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    # clouds
    for lu in left_up_clouds:
        for i in cloud_coords:
            pygame.draw.ellipse(screen, WHITE, [lu[0] + i[0], lu[1] + i[1], 30, 20])
    for i in range(len(left_up_clouds)):
        left_up_clouds[i][0] += v_clouds / FPS
        if left_up_clouds[i][0] > SIZE[0]:
            left_up_clouds[i][0] = -2 * cloud_coords[-1][0]

    # bounds
    for i in bounds_coords:
        pygame.draw.line(screen, WHITE, i[0], i[1], i[2])

    # safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    # yard line goal boxes
    for i in yard_lines:
        pygame.draw.line(screen, WHITE, *i)

    # score board
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)

    # goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    for i in goal_lines:
        pygame.draw.line(screen, WHITE, i[0], i[1], 3)

    # light poles
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    # lights
    for i in range(5):
        pygame.draw.ellipse(screen, light_color, [590 + i * 20, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [590 + i * 20, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [110 + i * 20, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [110 + i * 20, 20, 20, 20])
    for i in range(3):
        pygame.draw.line(screen, GRAY, [590, 60 - i * 20], [690, 60 - i * 20], 2)
        pygame.draw.line(screen, GRAY, [110, 60 - i * 20], [210, 60 - i * 20], 2)

    # net
    for i in range(31):
        pygame.draw.line(screen, WHITE, [325 + i * 5, 140], [int(341 + i * 118 / 30), 200], 1)
    for i in range(9):
        pygame.draw.line(screen, WHITE, [320, 140], [324 + i * 2, 216 - i * 2], 1)
        pygame.draw.line(screen, WHITE, [480, 140], [476 - i * 2, 216 - i * 2], 1)
    lu, ru, ld, rd = [324, 144], [476, 144], [335, 200], [465, 200]
    cnt = 14
    for i in range(cnt):
        pygame.draw.line(screen, WHITE,
                         [lu[0] + int((ld[0] - lu[0]) / cnt * i), lu[1] + int((ld[1] - lu[1]) / cnt * i)],
                         [ru[0] + int((rd[0] - ru[0]) / cnt * i), ru[1] + int((rd[1] - ru[1]) / cnt * i)], 1)

    for i in polygons:
        pygame.draw.polygon(screen, i[0], i[1])

    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)

    pygame.draw.ellipse(screen, GRAY, [*man, 30, 30])
    pygame.draw.ellipse(screen, BLACK, [*man, 30, 30], 3)
    for i in man_lines:
        pygame.draw.line(screen, BLACK, [man[0] + i[0], man[1] + i[1]], [man[0] + i[2], man[1] + i[3]], i[4])

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))
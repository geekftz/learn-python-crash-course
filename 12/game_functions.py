import sys

import pygame

def check_events(ship):
    # respond to keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # move ship to the left
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(ai_settings, screen, ship):
    # update the image on the screen and switch a new screen
    # redraw screen in every loop
    screen.fill(ai_settings.bg_color)

    ship.blitme()

    # make the recently drawn screen visible
    pygame.display.flip()
import sys

import pygame
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # start the main loop of the game
    while True:
        # observer keyboard events and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("sys exit")
                sys.exit()

        # redraw screen in every loop
        screen.fill(ai_settings.bg_color)

        # make the recently drawn screen visible
        pygame.display.flip()
run_game()
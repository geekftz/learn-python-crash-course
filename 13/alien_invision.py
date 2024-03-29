import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create an instance for storing game statistics
    stats = GameStats(ai_settings)

    # create a ship
    ship = Ship(ai_settings, screen)

    # create a group to store bullets
    bullets = Group()

    aliens = Group()

    # create aliens group
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # start the main loop of the game
    while True:
        # observer keyboard events and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets)



run_game()
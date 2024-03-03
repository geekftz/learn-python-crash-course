import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep


# old code
# def check_events(ship):
#     # respond to keyboard and mouse events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 # move ship to the right
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 # move ship to the left
#                 ship.moving_left = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False

# refactor code
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()



def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game dynamic settings
        ai_settings.initialize_dynamic_settings()

        # hide cursor
        pygame.mouse.set_visible(False)

        # reset game statistics info
        stats.reset_stats()
        stats.game_active = True

        # clear aliens list and bullets list
        aliens.empty()
        bullets.empty()

        # create a new group of aliens, make center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button):
    # update the image on the screen and switch a new screen
    # redraw screen in every loop
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # if game is not active, draw play button
    if not stats.game_active:
        play_button.draw_button()

    # make the recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # delete disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)



def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # check if any bullets have hit the alien
    # if that's the case, delete the corresponding bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """ create alien fleet """
    # create an alien, and calculate how many aliens can be accommodated in a row
    # the distance between aliens is the width of alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    print(number_rows)

    # create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # create an alien and add it to the current row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def check_fleet_edges(ai_settings, aliens):
    """take corresponding measures when alien reach the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    """move the aliens fleet to the bottom, change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check the corresponding between aliens and ships
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Ship hit")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # check if any aliens reached to the bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to the ship hit by aliens"""
    # reduce ships_left by one
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # empty the aliens list and bullets list
        aliens.empty()
        bullets.empty()

        # create a group of new aliens, and put the ship in the center at the bottom of the screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

























import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # initialize ship and set initial position
        self.screen = screen

        self.ai_settings = ai_settings

        # load ship images and obtain their bounding rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each ship in the center at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal values in the attribute center of the ship
        self.center = float(self.rect.centerx)

        # moving signs
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # adjust the position of the ship according to the moving signs
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object according to the self.center
        self.rect.centerx = self.center

    def blitme(self):
        # draw ship at the designated position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx



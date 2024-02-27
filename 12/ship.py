import pygame


class Ship():
    def __init__(self, screen):
        # initialize ship and set initial position
        self.screen = screen

        # load ship images and obtain their bounding rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each ship in the center at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        # draw ship at the designated position
        self.screen.blit(self.image, self.rect)


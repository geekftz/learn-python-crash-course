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

        # moving signs
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # adjust the position of the ship according to the moving signs
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        # draw ship at the designated position
        self.screen.blit(self.image, self.rect)


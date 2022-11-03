from random import randint

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):


    def __init__(self, sideways_game):

        super().__init__()
        self.screen = sideways_game.screen
        self.settings = sideways_game.settings


        self.image = pygame.image.load('../images/shipPink_manned.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at a random position on the right side
        #   of the screen.
        self.rect.left = self.screen.get_rect().right
        # The farthest down the screen we'll place the alien is the height
        #   of the screen, minus the height of the alien.
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien steadily to the left."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
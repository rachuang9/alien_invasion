import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __int__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('')

        
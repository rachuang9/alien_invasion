import pygame
from pygame.sprite import Sprite


class Star(Sprite):


    def __init__(self, stars_game):

        super().__init__()
        self.screen = stars_game.screen


        self.image = pygame.image.load('../Homework/star.bmp')
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.y = float(self.rect.y)
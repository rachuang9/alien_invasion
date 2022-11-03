import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):

    def __init__(self, rd_game):

        super().__init__()
        self.raindrop_speed = .3
        self.screen = rd_game.screen
        self.settings = rd_game.settings


        self.image = pygame.image.load('../Homework/raindrop.bmp')
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.y = float(self.rect.y)

    def check_disappeared(self):

        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):

        self.y += self.raindrop_speed
        self.rect.y = self.y

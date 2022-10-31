import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, sideways_game):
        super().__init__()

        self.screen = sideways_game.screen
        self.bullet_color = (60, 60, 60)

        # settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_speed = 1.5
        self.bullets_allowed = 3


        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = sideways_game.ship.rect.midright



        self.x = float(self.rect.x)


    def update(self):
        """move the bullet across the screen"""
        # update the decimal position of the bullet
        self.x += self.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)



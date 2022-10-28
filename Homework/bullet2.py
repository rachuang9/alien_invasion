import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, sideways_game):
        super().__init__()

        self.screen = sideways_game.screen
        self.bullet_color = (60, 60, 60)

        # settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.0
        self.bullets_allowed = 3

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = sideways_game.ship.rect.midright


        #store the bullets position as a decimal value
        self.x = float(self.rect.x)

        #self.bullet = False
        #self.screen = pygame.display.set_mode((1100, 700))
        #self.bullets = pygame.sprite.Group()

    def update(self):
        """move the bullet across the screen"""
        # update the decimal position of the bullet
        self.x += self.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)



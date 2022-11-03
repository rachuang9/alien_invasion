import pygame


class Ship:


    def __init__(self, sideways_game):

        self.screen = sideways_game.screen
        self.settings = sideways_game.settings
        self.screen_rect = sideways_game.screen.get_rect()


        self.image = pygame.image.load('../Homework/rocket.bmp')
        self.rect = self.image.get_rect()


        self.center_ship()


        self.moving_up = False
        self.moving_down = False

    def update(self):

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        self.rect.y = self.y

    def center_ship(self):

        self.rect.midleft = self.screen_rect.midleft


        self.y = float(self.rect.y)

    def blitme(self):

        self.screen.blit(self.image, self.rect)
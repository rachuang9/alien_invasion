import pygame


class Ship:

    def __init__(self, rr_game):
        self.screen = rr_game.screen
        self.screen_rect = rr_game.screen.get_rect()

        self.image = pygame.image.load('../Homework/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

        self.rocket_speed = 1.5

    def update(self):
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        # self.x += 1
        # if self.moving_left and self.rect.left > 0:
        # self.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rocket_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame

class Ship:

    def _init_(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect= self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image, self.rect)

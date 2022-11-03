import sys
import pygame
from settings_h import Settings
from raindrop import Raindrop


class RaindropGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop")

        self.raindrop = pygame.sprite.Group()
        self._create_raindrops()

    def run_game(self):

        while True:
            self._check_events()
            self.raindrop.update()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.Quit:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self,event):

        if event.key == pygame.K_q:
            sys.exit()

    def _create_raindrops(self):

        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = (self.settings.screen_height - (2 * raindrop_height))
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        available_space_y = (self.settings.screen_height - (2 * raindrop_height))
        number_rows = available_space_y // (2 * raindrop_height)
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)


    def _create_raindrop(self, raindrop_number, row_number):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.y = raindrop.y
        raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number

        self.raindrop.add(raindrop)

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self.raindrop.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':

    r_game = RaindropGame()
    r_game.run_game()
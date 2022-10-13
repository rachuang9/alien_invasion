import pygame
import sys
from settings import settings
class AlienInvasion:

    def_init_(self):
        pygame.init()
        self.settings=settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color=(230,230,230)
    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit()
            self.screen.fill(self.settingss.bg.color)
            pygame.display.flip()


if_name_== '_main_':
    ai = AlienInvasion()
    ai.run_game()

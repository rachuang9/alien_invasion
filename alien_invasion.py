import pygame
import sys
class AlienInvasion:

    def_init_(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color=(230,230,230)
    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit()
            self.screen.fill(self.bg.color)
            pygame.display.flip()

if_name_== '_main_':
    ai = AlienInvasion()
    ai.run_game()

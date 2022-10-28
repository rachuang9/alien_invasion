import sys
import pygame
from bullet2 import Bullet
from rocket import Ship
from settings_h import Settings


class Rocket:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("sideways shooter")
        # self.rect.midleft = self.settin.get_rect().midleft
        # self.display_rect = display.get_rect()
        # self.rocket_speed = 1.5
        # self.y = float(self.rect.y)
        # self.bg_color = (200, 200, 200)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):

        if event.key == pygame.K_UP:

            self.ship.moving_up = True
            print("Moving up")
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            print("Moving down")
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bullets(self):
        self.bullets.update()
        # get rid of bullets that are off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _fire_bullet(self, bullets_allowed=4):
        if len(self.bullets) < bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    sideways_game = Rocket()
    sideways_game.run_game()

# pygame.init()
# screen = pygame.display.set_mode((100, 100))
# pygame.display.set_caption("sideways shooter")
# ship = Rocket(screen)
# ship.update()
# screen.fill((24, 30, 92))
# ship.draw()
# pygame.display.flip()

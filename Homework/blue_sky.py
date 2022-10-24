import sys

import pygame
import time


# game character
#class Character:
    #def __init__(self, screen):
        #self.character_rect = screen.get_rect()
        #self.character = pygame.image.load('../images/shipPink_manned.bmp')
        #self.screen_rect = screen.get_rect()
        #self.rect = self.character.get_rect()
        #self.screen_rect.center = self.character_rect.center
        #self.character_rect = self.character.get_rect(center=screen.get_rect().center)

    #def blitme(self):
        #self.screen.blit(self.character, self.character_rect)





class Rocket:
    def __init__(self, screen):
        self.rocket_rect = screen.get_rect()
        self.screen = screen
        self.rocket = pygame.image.load('../images/ship.bmp')
        self.screen_rect = screen.get_rect()
        self.rect = self.rocket.get_rect()
        self.screen_rect.center = self.rocket_rect.center
        self.rocket_rect = self.rocket.get_rect(center=screen.get_rect().center)
        self.rocket_speed = 1.5
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
            print("I am moving right")
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
            print("I am moving left")
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.rocket, self.rocket_rect)


pygame.init()
screen = pygame.display.set_mode((200, 200))
rocket = Rocket(screen)
pygame.display.flip()
rocket.blitme()
rocket.update()
screen.fill((0, 0, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            rocket.moving_down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            rocket.moving_down = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            rocket.moving_up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            rocket.moving_up = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            rocket.moving_left = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            rocket.moving_left = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            rocket.moving_right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            rocket.moving_right = False
    rocket.update()

    rocket.blitme()
    pygame.display.flip()
#character = Character(screen)
#character.blitme()

time.sleep(8)

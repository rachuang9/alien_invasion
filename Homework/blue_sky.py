import sys
import pygame
from pygame.sprite import Sprite
import time

# game character
# class Character:
# def __init__(self, screen):
# self.character_rect = screen.get_rect()
# self.character = pygame.image.load('../images/shipPink_manned.bmp')
# self.screen_rect = screen.get_rect()
# self.rect = self.character.get_rect()
# self.screen_rect.center = self.character_rect.center
# self.character_rect = self.character.get_rect(center=screen.get_rect().center)

# def blitme(self):
# self.screen.blit(self.character, self.character_rect)




class Rocket:
    def __init__(self, screen):

        self.rocket_rect = screen.get_rect()
        self.screen = screen
        self.rocket = pygame.image.load('../images/rocket.bmp')
        self.screen_rect = screen.get_rect()
        self.rect = self.rocket.get_rect()
        self.screen_rect.center = self.rocket_rect.center


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False









    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 1




        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.rocket, self.rect)



pygame.init()
display_width = 200
display_height = 200

gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)

rocket = Rocket(gameDisplay)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.moving_left = True
                print("I am moving to the left")
            elif event.key == pygame.K_RIGHT:
                rocket.moving_right = True
                print("I am moving to the right")
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
                print("I am moving down")
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
                print("I am moving up")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocket.moving_left = False
                print("I stopped moving left")
                rocket.moving_right = False
                print("I stopped moving right")
            if event.key == pygame.K_DOWN or event.key == pygame.KEYUP:
                rocket.moving_down = False
                print("I stopped moving down")
                rocket.moving_up = False
                print("I am stopped moving up")


    rocket.update()
    gameDisplay.fill(white)

    rocket.blitme()
    pygame.display.flip()
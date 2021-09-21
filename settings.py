#Settings file

import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Create the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        bar_height = 75
        bar_width = 25
        self.surf = pygame.Surface((bar_width, bar_height))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(bar_width, SCREEN_HEIGHT/2-bar_height/2)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -8)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 8)
    
        # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Create the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        ball_diameter = 10
        self.surf = pygame.Surface((ball_diameter, ball_diameter))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        )

        self.hor_speed = 3
        self.ver_speed = random.randrange(-5,6,2)
        if self.ver_speed == 0:
            self.ver_speed = 5

    def update(self, alert):
        if alert == 1:
            self.hor_speed = - self.hor_speed
            self.ver_speed = random.randrange(-5,7,2)
        if alert == 2:
            self.hor_speed = - self.hor_speed
            self.ver_speed = - random.randrange(-5,7,2)
        
        self.rect.move_ip(self.hor_speed, self.ver_speed)

        if self.rect.top <= 0:
            self.ver_speed = - self.ver_speed
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
        if self.rect.bottom > SCREEN_HEIGHT:
            self.ver_speed = - self.ver_speed
        if self.rect.right < 0:
            self.kill()

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        bar_height = 75
        bar_width = 25
        self.surf = pygame.Surface((bar_width, bar_height))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH-bar_width*2, SCREEN_HEIGHT/2-bar_height/2)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(0, -8)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(0, 8)
    
        # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
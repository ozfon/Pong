#Settings file

import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
)

#Create the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.bar_height = 75
        self.bar_width = 25
        self.surf = pygame.Surface((self.bar_width, self.bar_height))
        self.surf.fill(('BLUE'))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.bar_width, SCREEN_HEIGHT//2-self.bar_height//2)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
    
        # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def restart(self):
        self.rect.update(self.bar_width, SCREEN_HEIGHT//2-self.bar_height//2, self.bar_width, self.bar_height)

#Create the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.diameter = 10
        self.surf = pygame.Surface((self.diameter, self.diameter))
        self.surf.fill(('GREEN'))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        )

        self.hor_speed = random.choice([3,-3])
        self.ver_speed = random.randrange(-3,4,2)
        if self.ver_speed == 0:
            self.ver_speed = 5
        self.counter = 0

    def update(self, alert):
        if alert == 1:
            self.hor_speed = - self.hor_speed
            self.ver_speed = random.randrange(-5,7,2)
            if self.counter % 5 == 4:
                if self.hor_speed < 0:
                    self.hor_speed -= 1
                else:
                    self.hor_speed += 1
        if alert == 2:
            self.hor_speed = - self.hor_speed
            self.ver_speed = - random.randrange(-5,7,2)
            if self.counter % 5 == 4:
                if self.hor_speed < 0:
                    self.hor_speed -= 1
                else:
                    self.hor_speed += 1
        
        self.rect.move_ip(self.hor_speed, self.ver_speed)

        if self.rect.top <= 0:
            self.ver_speed = - self.ver_speed
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
        if self.rect.bottom > SCREEN_HEIGHT:
            self.ver_speed = - self.ver_speed
        if self.rect.right < 0:
            self.kill()

    def restart(self):
        self.rect.update(SCREEN_WIDTH//2-self.diameter//2, SCREEN_HEIGHT//2-self.diameter//2, self.diameter, self.diameter)

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.bar_height = 75
        self.bar_width = 25
        self.surf = pygame.Surface((self.bar_width, self.bar_height))
        self.surf.fill(('RED'))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH-self.bar_width*2, SCREEN_HEIGHT/2-self.bar_height/2)
        self.speed = 7

    # Move the sprite based on user keypresses
    def update(self, dir):
        if dir == 1:
            self.rect.move_ip(0, self.speed)
        elif dir == 2:
            self.rect.move_ip(0, -self.speed)
        else:
            pass
    
        # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def restart(self):
        self.rect.update(SCREEN_WIDTH-self.bar_width*2, SCREEN_HEIGHT//2-self.bar_height//2, self.bar_width, self.bar_height)
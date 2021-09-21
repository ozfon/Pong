import pygame
import random
from settings import *

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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

def draw_screen():
    screen.fill(('BLACK'))

def obj_update(pressed_keys):
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    opponent.update(pressed_keys)

def collide_check(obj1, obj2):
    if pygame.sprite.spritecollideany(obj1, obj2):
        if obj1 == player:
            ball.update(1)
        else:
            ball.update(2)
    else:
        ball.update(0)
    
FPS = 60

# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Instantiate. Right now, this is just a rectangle.
player = Player()
ball = Ball()
opponent = Opponent()

balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
opponents = pygame.sprite.Group()
balls.add(ball)
opponents.add(opponent)
all_sprites.add(opponents)
all_sprites.add(player)
all_sprites.add(ball)


def main():
    clock = pygame.time.Clock()
    
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        
        draw_screen()

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        obj_update(pressed_keys)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        collide_check(player, balls)
        collide_check(opponent, balls)

        if len(balls) == 0:
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__": #only runs main function if this file is ran directly
    main()
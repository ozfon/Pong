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

clock = pygame.time.Clock()

# Initiate player. Right now, this is just a rectangle.
player = Player()
ball = Ball()

# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

balls = pygame.sprite.Group()
balls.add(ball)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ball)


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        
        clock.tick(60)

        screen.fill((0, 0, 0))

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()

        if pygame.sprite.spritecollideany(player, balls):
            # change the ball direction
            ball.update(1)
        else:
            ball.update(0)

    pygame.quit()

if __name__ == "__main__": #only runs main function if this file is ran directly
    main()
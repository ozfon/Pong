import pygame
from settings import SCREEN_WIDTH,SCREEN_HEIGHT

def go():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    pygame.font.init()

    screen.fill(('Black'))

    return clock, screen
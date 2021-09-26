import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, Player, Ball, Opponent
from startup import go
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_RETURN
)

def start():
    clock, screen = go()

    #text
    titlefont = pygame.font.SysFont('Comic Sans MS', 30)
    title = titlefont.render('Pong', True, ('BLUE'))
    instruction = titlefont.render('Hit Enter to Start', True, ('White'))
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2,SCREEN_HEIGHT // 4)
    screen.blit(title, titleRect)
    insRect = instruction.get_rect()
    insRect.center = (SCREEN_WIDTH // 2,SCREEN_HEIGHT // 3)
    screen.blit(instruction, insRect)
    controls = titlefont.render('UP key - move up & DOWN key - move down', True, ('WHITE'))
    controlsRect = controls.get_rect()
    controlsRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)
    screen.blit(controls, controlsRect)


    # Instantiate
    player = Player()
    ball = Ball()
    opponent = Opponent()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(opponent)
    all_sprites.add(player)
    all_sprites.add(ball)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    stop = True
                if event.key == K_RETURN:
                    running = False
                    stop = False

            elif event.type == QUIT:
                running = False
                stop = True
        
        pygame.display.update()

    pygame.quit()

    return stop
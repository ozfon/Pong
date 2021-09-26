import pygame
import time
from settings import SCREEN_HEIGHT,SCREEN_WIDTH,Player,Ball,Opponent,FPS
from startup import go
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def play():

    def draw_screen():
        screen.fill(('BLACK'))
        gamefont = pygame.font.SysFont('Comic Sans MS', 12)

        spdtxt = gamefont.render('Ball Speed: ' + str(abs(ball.hor_speed)), True, ('GREEN'))
        spdtxtRect = spdtxt.get_rect()
        spdtxtRect.midtop = (SCREEN_WIDTH//2, 5)
        screen.blit(spdtxt, spdtxtRect)

        plyscore = gamefont.render('Player Score: ' + str(player_score), True, ('BLUE'))
        plyscoreRect = plyscore.get_rect()
        plyscoreRect.topleft = (5, 5)
        screen.blit(plyscore, plyscoreRect)

        oppscore = gamefont.render('Opponent Score: ' + str(opponent_score), True, ('RED'))
        oppscoreRect = oppscore.get_rect()
        oppscoreRect.topright = (SCREEN_WIDTH-5, 5)
        screen.blit(oppscore, oppscoreRect)        

    def player_update(pressed_keys):
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
    
    def opp_update():
        if ball.rect.center[1] > opponent.rect.center[1]:
            dir = 1
        elif ball.rect.center[1] < opponent.rect.center[1]:
            dir = 2
        else:
            dir = 3
        opponent.update(dir)

    def collide_check(obj1, obj2):
        if pygame.sprite.spritecollideany(obj1, obj2):
            if obj1 == player:
                ball.update(1)
                ball.counter += 1
            else:
                ball.update(2)
                ball.counter += 1
        else:
            ball.update(0)

    # Initialize pygame
    clock, screen = go()
    player_score = 0
    opponent_score = 0
    player_score_counter = True
    opponent_score_counter = True
    
    # Instantiate
    player = Player()
    ball = Ball()
    opponent = Opponent()

    # Setup groups
    balls = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    opponents = pygame.sprite.Group()
    balls.add(ball)
    opponents.add(opponent)
    all_sprites.add(opponents)
    all_sprites.add(player)
    all_sprites.add(ball)

    clock = pygame.time.Clock()
    
    playing = True
    wait = False

    while playing:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    playing = False
            elif event.type == QUIT:
                playing = False
        
        draw_screen()

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        player_update(pressed_keys)
        opp_update()

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        collide_check(player, balls)
        collide_check(opponent, balls)

        if wait == True:            
            #restart game
            opponent.restart()
            player.restart()
            wait = False
            ball = Ball()
            balls.add(ball)
            all_sprites.add(ball)
            player_score_counter = True
            opponent_score_counter = True
            time.sleep(1)
        if len(balls) == 0:
            wait = True
        if opponent_score_counter == True and ball.rect.left < 0:
            opponent_score_counter = False
            opponent_score += 1
        if player_score_counter == True and ball.rect.right > SCREEN_WIDTH:
            player_score_counter = False
            player_score += 1

        pygame.display.flip()

    pygame.quit()
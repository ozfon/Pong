#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
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

        spdtxt = gamefont.render('Ball Speed: ' + str(abs(ball.hor_speed)), True, ('WHITE'))
        spdtxtRect = spdtxt.get_rect()
        spdtxtRect.midtop = (SCREEN_WIDTH//2, 5)
        screen.blit(spdtxt, spdtxtRect)

        plyscore = gamefont.render('Player Score: ' + str(0), True, ('GREEN'))
        plyscoreRect = plyscore.get_rect()
        plyscoreRect.topleft = (5, 5)
        screen.blit(plyscore, plyscoreRect)

        oppscore = gamefont.render('Opponent Score: ' + str(0), True, ('RED'))
        oppscoreRect = oppscore.get_rect()
        oppscoreRect.topright = (SCREEN_WIDTH-5, 5)
        screen.blit(oppscore, oppscoreRect)        

    def obj_update(pressed_keys):
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        opponent.update(pressed_keys)

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

        obj_update(pressed_keys)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        collide_check(player, balls)
        collide_check(opponent, balls)

        if len(balls) == 0:
            playing = False

        pygame.display.flip()

    pygame.quit()

# filename __init__ is required to treat scripts folder as resource

# graphics init

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# variable for size of field in graphics in px
blocksize = 30
# var for number of blocks in row of simulation
N = 10

WINDOW_WIDTH = blocksize * N
WINDOW_HEIGHT = blocksize * N

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('UberKelner')

WHITE = (255, 255, 255)

all_sprites_list = pygame.sprite.Group()

# walls = [Wall(300,i*100) for i in range(4)] + [Wall(600,i*100+200) for i in range(4)]

# for wall in walls:
#     all_sprites_list.add(wall)

# elsa = Elsa(0,0, WINDOW_WIDTH, WINDOW_HEIGHT, walls)
# all_sprites_list.add(elsa)
# anna = Anna(800,300, WINDOW_WIDTH, WINDOW_HEIGHT)
# all_sprites_list.add(anna)

# hans = HansX(300,400, WINDOW_WIDTH, WINDOW_HEIGHT)
# all_sprites_list.add(hans)

# olafs = [Olaf(0,500),Olaf(300,400), Olaf(600,0), Olaf(800,150)]
# for olaf in olafs:
#    all_sprites_list.add(olaf)

# background_image = pygame.image.load("images/background.png")
# gameover_image = pygame.image.load("images/gameover.png")
# fail_image = pygame.image.load("images/fail.png")

gamestate = 0

pygame.mixer.init()
pygame.mixer.music.load('sounds/over.mp3')

olaf_sound = pygame.mixer.Sound('sounds/olaf.wav')

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            print(pygame.key.name(event.key))
            if event.key == K_RIGHT:
                elsa.move_right()
                hans.move()
            elif event.key == K_LEFT:
                elsa.move_left()
                hans.move()
            elif event.key == K_DOWN:
                elsa.move_down()
                hans.move()
            elif event.key == K_UP:
                elsa.move_up()
                hans.move()
            elif event.key == K_r:
                gamestate = 0
                pygame.mixer.music.stop()

            elif pygame.key.name(event.key) == "w":
                elsa.move_up()



    all_sprites_list.update()

    if pygame.sprite.collide_rect(elsa, anna):
        gamestate = 1
        pygame.mixer.music.play(-1)
        elsa.reset()

    if pygame.sprite.collide_rect(elsa, hans):
        gamestate = 2
        elsa.reset()

    for olaf in olafs:
        if pygame.sprite.collide_rect(elsa, olaf):
            all_sprites_list.remove(olaf)
            olaf.rect.x=-1000
            olaf.rect.y=-1000
            olaf_sound.play()

    # game state control - win loose nothing
    if gamestate == 0:
        DISPLAYSURF.blit(background_image, (0,0))
        all_sprites_list.draw(DISPLAYSURF)
    elif gamestate == 1:
        DISPLAYSURF.blit(gameover_image, (0,0))
    elif gamestate == 2:
        DISPLAYSURF.blit(fail_image, (0,0))


    #Refresh Screen
    pygame.display.flip()
    fpsClock.tick(FPS)

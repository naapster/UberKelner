


# main game script controller:

# init
from scripts.__init__ import *
from scripts.dinning_table import *

from scripts.matrix import Matrix

# kelner
from scripts.waiter import Waiter

import pygame
import sys

if __name__ == '__main__':

    # example usage of matrix, for development purpose only
    """mat = Matrix(N, N)
    mat.print_matrix()
    mat.insert_object('asdasd', 2, 4, debug=True)
    mat.insert_object(Matrix(2, 2, fill=5), 1, 1)
    mat.print_matrix()
    print(mat.objects_to_list('asdasd'))
    mat.delete_object(1, 1, debug=True)
    mat.print_matrix()"""

    # main game loop

    # Restaurant - space of simulation, Uber - agent of simulation
    # = Matrix(N, N)
    Uber = Waiter(20, 30)

    #gamestates: 1 - simulation running, 0 - simulation finished
    gamestate = 1

    #to tylko robie dla testu czy to będzie wyświetlać się


    all_sprites = pygame.sprite.Group()

    tables = [Dinning_table(300,i*100) for i in range(1)] + [Dinning_table(600,i*100+200) for i in range(1)]

    for table in tables:
        all_sprites.add(table)


    while gamestate != 0:  # the main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                gamestate = 0
            elif event.type == KEYUP:
                #control check for development purpose only
                print(pygame.key.name(event.key))
                if event.key == K_RIGHT:
                    Uber.move_right()
                elif event.key == K_LEFT:
                    Uber.move_left()
                elif event.key == K_DOWN:
                    Uber.move_down()
                elif event.key == K_UP:
                    Uber.move_up()
                elif event.key == K_r:
                    gamestate = -1
                    while gamestate == -1:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                gamestate = 0
                            elif event.type == KEYUP:
                                if event.key == K_r:
                                    gamestate = 1

        # simulation sprites control - to be added


        all_sprites.draw(DISPLAYSURF)
        # Refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)

    # end of main loop: close simulation
    pygame.quit()
    sys.exit()
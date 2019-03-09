
# main game script controller:

# init
from scripts.__init__ import *

# matrix
from scripts.matrix import Matrix

# kelner
from scripts.waiter import Waiter

if __name__ == '__main__':
    mat = Matrix(N, N)
    mat.print_matrix()
    mat.insert_object('asdasd', 2, 4, debug=True)
    mat.insert_object(Matrix(2, 2, fill=5), 1, 1)
    mat.print_matrix()
    print(mat.objects_to_list('asdasd'))
    mat.delete_object(1, 1, debug=True)
    mat.print_matrix()

    # main game loop

    # Restaurant - space of simulation, Uber - agent of simulation
    Restaurant = Matrix(N, N)
    Uber = Waiter(0,0)

    #gamestates: 1 - simulation running, 0 - simulation stopped, (-1) - simulation finished
    gamestate = 1

    while gamestate:  # the main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                gamestate = 1
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
                    gamestate = 0

        all_sprites_list.update()

        # game state control - win loose nothing
        if gamestate == 0:
            DISPLAYSURF.blit(background_image, (0, 0))
            all_sprites_list.draw(DISPLAYSURF)
        elif gamestate == 1:
            DISPLAYSURF.blit(gameover_image, (0, 0))
        elif gamestate == 2:
            DISPLAYSURF.blit(fail_image, (0, 0))

        # Refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)

    # end of main loop: close simulation
    pygame.quit()
    sys.exit()
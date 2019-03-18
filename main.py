# main game script controller:

# init
from scripts.waiter import *
import sys
import pygame
from pygame.locals import *

if __name__ == '__main__':

    # init random coordinates
    random_coordinates = create_random_coordinates()

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(random_coordinates, 8, 2)

    # list of all sprites for graphics window to draw
    all_sprites = pygame.sprite.Group()

    # add sprites to draw to the list - REPAIR
    all_sprites.add(Uber)
    for table in Uber.restaurant.objects_to_list(Dinning_table(0, 0)):
        all_sprites.add(table[0])
    for furnace in Uber.restaurant.objects_to_list(Furnace(0, 0)):
        all_sprites.add(furnace[0])

    # main game loop
    pygame.event.clear()
    while True:  # the main game loop
        # wait for key pressed:
        for event in pygame.event.get():
            # end of main loop: close simulation
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # after key was pressed:
            elif event.type == KEYUP:
                # exit simulation:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # or run new round for environment
                Uber.next_round(event.key)
                # WARNING
                # in the future release, on key pressed no event key will be passed
                # and the waiter will have to choose the action on his own

        # simulation sprites control
        all_sprites.update()
        # draw background
        DISPLAYSURF.fill(WHITE)
        # draw sprites
        all_sprites.draw(DISPLAYSURF)
        # Refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)
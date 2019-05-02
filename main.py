#!/usr/bin/python
# -*- coding: utf-8 -*-

# simulation controller:

import datetime
# solve pygame audio driver error
import os
from os import path
from random import shuffle

from scripts.waiter import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'

# filename __init__ is required to treat scripts folder as resource
# variables:
# size of sprites in px
blocksize = 60
# sprite constants
SPRITE_FOLDER = 'images'
SPRITE_EXTENSION = '.png'


# init sprite sprite_name on coordinate x, y
def init_graphics(self, x, y, sprite_name):
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # init graphics - do not touch!
    pygame.sprite.Sprite.__init__(self)
    # set image
    self.image = pygame.image.load(path.join(SPRITE_FOLDER, sprite_name + SPRITE_EXTENSION))
    # resize image to blocksize
    self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
    # set coordinates
    self.rect = self.image.get_rect()
    self.rect.x = x * blocksize
    self.rect.y = y * blocksize
    # //////////////////////////////////////////////////


# generate random positions list for all objects
def create_random_coordinates():
    # list of all possible numbers of coordinate
    _ = range(N)
    # cartesian product of all possible numbers
    matrix_fields = [[posX, posY] for posX in _ for posY in _]
    # randomize order of coordinates
    shuffle(matrix_fields)
    return matrix_fields


def luncher():
    possible_arguments = ['depthfs', 'breadthfs', 'bestfs']
    for index, arg in enumerate(possible_arguments):
        print('{0}. {1}'.format(index, arg))
    choice = input('----------\nPlese choose path finding algorithm. Use index of algorithm: ')
    try:
        return possible_arguments[int(choice)]
    except IndexError:
        print('Algorithm with this index doesn\'t exist')
        input()
        quit(410)


if __name__ == '__main__':
    alg_choice = luncher()

    print("Main: simulation controller executed...")

    # init list of variables, common for all simulations:
    # default settings
    control = True
    run_simulation = -1
    solution = "depthfs"
    FPS = 30
    # amount of blocks in row of simulation - not currently active, change init
    N = 5
    # number of tables
    num_tables = 0
    # number of furnaces
    num_furnaces = 1
    # number of walls
    num_walls = 10

    # parse arguments
    '''
    print("Main: Parsing arguments")
    parser = ArgumentParser()
    
    # REPAIR - PROSZĘ NAPISAĆ OBSŁUGĘ ARGUMENTÓW ŻEBY APLIKACJA BYŁA OBSŁUGIWANA
    # TAK JAK W PRZYKŁADOWYM KOMENTARZU NAD ARGUMENTEM
    
    # --size 10
    parser.add_argument("-n", "--size", dest="filename",
                        help="set size of simulation", metavar="INT+")
    # --fps 30
    parser.add_argument("-f", "--fps",
                        action="store_false", dest="verbose", default=True,
                        help="set frames per second of simulation")
                        
    # --random N num_tables num_furnaces num_walls       
    parser.add_argument("-r", "--random",
                        action="store_false", dest="verbose", default=True,
                        help="create random simulation")
                        
    # --log -1
    parser.add_argument("-l", "--log",
                        action="store_false", dest="verbose", default=True,
                        help="run simulation from log")
                        
    # --solution dfs
    parser.add_argument("-s", "--solution",
                        action="store_false", dest="verbose", default=True,
                        help="choose solving method. Deep-first search is the default choice.")
                        
    # --blocksize 60
    parser.add_argument("-b", "--blocksize",
                        action="store_false", dest="verbose", default=True,
                        help="set size of sprites (in px)")

    args = parser.parse_args()

    # run arguments
    if args.size:
        print("Args: Set size to %s" % args.size)
        N = args.size
    else:
        print("Main: Set size to ")

    # frames per second setting
    if args.fps:
        print("Args: Set fps to %s" % args.size)
        FPS = args.fps
    else:
        print("Main: Set fps to 30")
        FPS = 30

    # choose whether to run simulation from log (True) or generate random (False)
    if args.random:
        print("Args: Generating random simulation")
        control = False
    else:
        if args.log:
            print("Args: Generating simulation from %s log" % args.log)
            control = True
            run_simulation = args.log  # index of simulation to run in log list
        else:
            print("Main: log loig")

    if args.solution:
        print("Args: Set solution to %s" % args.solution)
        solution = args.solution
    else:
        print("Main: set solution method to dfs")
        solution = "dfs"
        
    if args.blocksize:
        print("Args: Set blocksize to %s" % args.blocksize)
        blocksize = args.blocksize
    else:
        print("Main: set blocksize to 60")
        blocksize = 60
    '''

    if control:
        # reload simulation state from log:
        # get last row in log
        with open("simulation_log.txt") as myfile:
            log = list(myfile)[run_simulation].split('\t')

        # amount of blocks in row of simulation - not currently active, change init
        N = int(log[1])
        # number of tables
        num_tables = int(log[2])
        # number of furnaces
        num_furnaces = int(log[3])
        # number of walls
        num_walls = int(log[4])
        # random coordinates
        _ = log[5].replace('[', '').split('],')
        coordinates = [list(map(int, s.replace(']', '').split(','))) for s in _]

    else:

        # generate random simulation:
        # random coordinates
        coordinates = create_random_coordinates()[:(num_tables + num_furnaces + num_walls + 1)]
        # rest of values are default

        # save state of simulation to file
        with open("simulation_log.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t'
                         + str(N) + '\t' + str(num_tables) + '\t' + str(num_furnaces) + '\t' + str(num_walls) + '\t'
                         + str(coordinates[:(num_tables+num_furnaces+num_walls+1)]) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(N, coordinates, num_tables, num_furnaces, num_walls)

    # list of all sprites for graphics window to draw
    all_sprites = pygame.sprite.Group()

    # add waiter to sprites list
    all_sprites.add(Uber)
    # add all tables and furnaces to sprites list
    for _ in Uber.restaurant.all_objects_to_list():
        all_sprites.add(_)

    # main game loop:

    # graphics init
    pygame.init()
    fpsClock = pygame.time.Clock()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((blocksize * N, blocksize * N), 0, 32)
    pygame.display.set_caption('UberKelner')
    WHITE = (255, 255, 255)

    # run solution seeking
    Uber.solve(alg_choice)

    # clear event log of game
    pygame.event.clear()
    # for eternity:
    control = True
    while control:
        # wait for key pressed:
        for event in pygame.event.get():
            # if [x] in right upper corner was clicked, exit game
            if event.type == QUIT:
                control = False
            # or after key was pressed:
            elif event.type == KEYUP:
                # exit simulation anyway:
                if event.key == K_ESCAPE:
                    control = False
                # or run new round for environment
                Uber.next_round(event.key)

        # simulation sprites control
        all_sprites.update()
        # draw background
        DISPLAYSURF.fill(WHITE)
        # draw sprites
        all_sprites.draw(DISPLAYSURF)
        # refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)

    print("Main: simulation controller execution complete.")
    pygame.quit()
    sys.exit()

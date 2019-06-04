#!/usr/bin/python
# -*- coding: utf-8 -*-

# simulation controller:

import datetime
import os
from random import shuffle
from argparse import ArgumentParser
from scripts.waiter import *
import pygame
from pygame.locals import *
import time

# solve pygame audio driver error
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# filename __init__ is required to treat scripts folder as resource
# variables:
# size of sprites in px
blocksize = 60
# graphics control
graphics = False
tests = ''

# init sprite sprite_name on coordinate x, y
def init_graphics(self, a, b, sprite_name):
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # init graphics - do not touch!
    pygame.sprite.Sprite.__init__(self)
    # set image
    self.image = pygame.image.load(path.join('images', sprite_name + '.png'))
    # resize image to blocksize
    self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
    # set coordinates
    self.rect = self.image.get_rect()
    self.rect.x = a * blocksize
    self.rect.y = b * blocksize
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


if __name__ == '__main__':
    print("Main: simulation controller executed...")
    # parse arguments
    print("Main: Parsing arguments:")
    description = "Project UberKelner\n Project goal: to create a static discrete environment corresponding " \
                  "to the real restaurant and the artificial intelligence agent serving as a waiter in the restaurant."
    parser = ArgumentParser(description=description)
    # --autorun True
    parser.add_argument("-a", "--autorun", help="run simulation steps automatically every one second",
                        required=False, default=False, type=bool)
    # REPAIR - blocksize changes for graphics window only, sprites still scale to original value (60 px)
    # --blocksize 60
    parser.add_argument("-b", "--blocksize", help="set size of sprites (in px)",
                        required=False, default=60, type=int)
    # --capture True
    parser.add_argument("-c", "--capture", help="capture screenshot of simulation",
                        required=False, default=False, type=bool)
    # --document "logs\simulation_log.txt"
    parser.add_argument("-d", "--document", help="set filename to read and write simulation logs",
                        required=False, default="data\simulation_log.txt", type=str)
    parser.add_argument("-f", "--fps", help="set frames per second of simulation",
                        required=False, default=30, type=int)
    # --graphics True
    parser.add_argument("-g", "--graphics", help="enable/disable use of graphics window and controls",
                        required=False, default=True, type=bool)
    # --log -1
    parser.add_argument("-l", "--log", help="choose row of document to read simulation",
                        required=False, default=-1, type=int)
    # --model True
    parser.add_argument("-m", "--model", help="create datamodel from simulation logs",
                        required=False, default=False, type=bool)
    # --size 10
    parser.add_argument("-n", "--size", help="set size of simulation",
                        required=False, default=10, type=int)
    # --random True
    parser.add_argument("-r", "--random", help="create random simulation with parameters: "
                                               "N num_tables num_furnaces num_walls",
                        required=False, default=False, type=bool)
    # --solution depthfs/breathfs/bestfs/all
    parser.add_argument("-s", "--solution",
                        help="choose solving method.\nMethods available: depthfs, breathfs, bestfs, all. \n"
                             "rabbit, svm, dtree.\nDeep-first search is the default choice.",
                        required=False, default="depthfs", type=str)

    # args will be a dictionary containing the arguments
    args = vars(parser.parse_args())
    # init list of variables, common for all simulations:
    blocksize = args['blocksize']
    # choose simulation log file
    simulation_log = args['document']
    FPS = args['fps']
    # row in simulation log to load - coordinates like in list, negative numbers mean positipon from the back of list
    run_simulation = args['log']
    model = args['model']
    # amount of blocks in row of simulation
    N = args['size']
    solution = args['solution']

    print("Args: Set autorun to %s" % args['autorun'])
    print("Args: Set blocksize to %s" % blocksize)
    print("Args: Set capture to %s" % args['capture'])
    print("Args: Set document to %s" % simulation_log)
    print("Args: Set FPS to %s" % FPS)
    print("Args: Set graphics to %s" % args['graphics'])
    print("Args: Set model to %s" % args['model'])
    print("Args: Set simulation log to %s" % run_simulation)
    print("Args: Set size to %s" % N)
    # print("Args: Set random to %s" % args['random'])
    print("Args: Set solution to %s" % solution)

    # default settings
    # number of tables
    num_tables = 0
    # number of furnaces
    num_furnaces = 1
    # number of walls
    num_walls = 10

    # if script was run to create model:
    if model:
        print("Model: model creation executed...")
        counter = 0

        # add header for scikit model
        header = "move, "
        for x in range(5):
            for y in range(5):
                header += "{}, ".format(str(x)+"x"+str(y))
        with open(path.join('data', 'datamodel_scikit.txt'), "w") as myfile:
            myfile.write(header + '\n')

        # for all files in logs:
        # for file in os.listdir(path.join('logs', 'temp')):
        for file in os.listdir(path.join('logs')):
            print("Model: calculating %s..." % file)
            # read file:
            if file.endswith(".txt"):
                with open(path.join('logs', file)) as f:
                    lines = f.readlines()
                    # for every log:
                    for log in lines:
                        if len(log) > 1:
                            print("\t for line %s..." % str(lines.index(log)+1))
                            try:
                                log = log.split('\t')
                                # reload simulation state from log:
                                # amount of blocks in row of simulation - not currently active, change init
                                N = int(log[1])
                                # number of tables
                                num_tables = int(log[2])
                                # number of furnaces
                                num_furnaces = int(log[3])
                                # number of walls
                                num_walls = int(log[4])
                                # coordinates
                                _ = log[5].replace('[', '').split('],')
                                coordinates = [list(map(int, s.replace(']', '').split(','))) for s in _]

                                # calculate simulation solution
                                Uber = Waiter(N, coordinates, num_tables, num_furnaces, num_walls, solution)

                                # run simulation:
                                while Uber.path:
                                    # parse neighbourhood with movement and save to datamodel
                                    Uber.parse_neighbourhood_to_model()
                                    # move agent on path
                                    Uber.next_round(K_SPACE)

                                del Uber

                                counter = counter + 1
                            except Exception as e:
                                # error occures when there are no elements of one kind
                                # (for example, map with no furnaces) therefore leaving empty list in log
                                print(e)
                        else:
                            print("\t encountered empty line (%s)" % str(lines.index(log)+1))
                f.close()
                print("Model: calculation of %s file completed." % file)

        print("Model: datamodel controller execution complete.")
        exit(0)

    if not args['random']:
        # reload simulation state from log:
        # get last row in log
        with open(simulation_log) as myfile:
            log = list(myfile)[run_simulation].split('\t')
        # amount of blocks in row of simulation - not currently active, change init
        N = int(log[1])
        # number of tables
        num_tables = int(log[2])
        # number of furnaces
        num_furnaces = int(log[3])
        # number of walls
        num_walls = int(log[4])
        # coordinates
        _ = log[5].replace('[', '').split('],')
        coordinates = [list(map(int, s.replace(']', '').split(','))) for s in _]

    else:
        # generate random simulation:
        # random coordinates
        coordinates = create_random_coordinates()[:(num_tables + num_furnaces + num_walls + 1)]
        # rest of values are default

        # save state of simulation to file
        with open(simulation_log, "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t'
                         + str(N) + '\t' + str(num_tables) + '\t' + str(num_furnaces) + '\t' + str(num_walls) + '\t'
                         + str(coordinates[:(num_tables + num_furnaces + num_walls + 1)]) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(N, coordinates, num_tables, num_furnaces, num_walls, solution)

    # main game loop:
    # check if graphics are enabled
    if args['graphics']:
        # graphics init
        # list of all sprites for graphics window to draw
        all_sprites = pygame.sprite.Group()
        # add waiter to sprites list
        all_sprites.add(Uber)
        # add all tables and furnaces to sprites list
        for _ in Uber.restaurant.all_objects_to_list():
            all_sprites.add(_)
        # create graphics window
        pygame.init()
        fpsClock = pygame.time.Clock()
        # set up the window
        DISPLAYSURF = pygame.display.set_mode((blocksize * N, blocksize * N), 0, 32)
        pygame.display.set_caption('UberKelner Realm')
        WHITE = (255, 255, 255)

        # clear event log of game
        pygame.event.clear()

        # run auto simulation
        if args['autorun']:
            uberpathlen = len(Uber.path)
            if uberpathlen > 1:
                print("Main: autorun started, estimated time of run: %s seconds" % uberpathlen)
            # set maximum number of steps
            upper_limit = Uber.n ** 2 * 2
            # while there is movement available
            while (uberpathlen > 0 or Uber.goals) and Uber.steps_count < upper_limit:
                # write comment
                if not uberpathlen % 10 and uberpathlen > 0:
                    print("Autorun: %s steps remaining..." % uberpathlen)
                # draw simulation
                all_sprites.update()
                # draw background
                DISPLAYSURF.fill(WHITE)
                # draw sprites
                all_sprites.draw(DISPLAYSURF)
                # refresh Screen
                pygame.display.flip()
                fpsClock.tick(FPS)
                # move agent
                Uber.next_round(K_SPACE)
                # every one second
                time.sleep(1 - time.time() % 1)
                # get next length
                uberpathlen = len(Uber.path)
            print("Main: autorun completed.")

        # save screenshot
        if args['capture']:
            pygame.image.save(DISPLAYSURF, path.join('documentation', 'screenshot.png'))
        # run manual simulation
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
                    # For generate moves to test
                    tests = Uber.get_test()


            # simulation sprites control
            all_sprites.update()
            # draw background
            DISPLAYSURF.fill(WHITE)
            # draw sprites
            all_sprites.draw(DISPLAYSURF)
            # refresh Screen
            pygame.display.flip()
            fpsClock.tick(FPS)
        # For save generated moves
        # with open('logs/test.txt', "a") as datatest:
        #   datatest.write('\n'+ str(tests))
        print("Main: simulation controller execution complete.")
        pygame.quit()
        sys.exit()

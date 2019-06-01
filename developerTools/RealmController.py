# map generating script

import datetime
from argparse import ArgumentParser


if __name__ == '__main__':

    print("RC: Realm controller executed...")
    # parse arguments
    print("RC: Parsing arguments:")
    description = "Realm Controller\n Project goal: to create a script to generate simulation logs from ASCII drawing" \
                  ", recreate ASCII maps from simulation logs and load drawings into logs."
    parser = ArgumentParser(description=description)
    # --control True
    parser.add_argument("-c", "--control",
                        help="set control variable. True - execute generator, False - execute recreation",
                        required=False, default=False, type=bool)
    # --document logs\simulation_log.txt
    parser.add_argument("-d", "--document", help="set filename to read and write simulation logs",
                        required=False, default="logs\simulation_log.txt", type=str)
    # --log -1
    parser.add_argument("-l", "--log", help="choose row of document to read simulation",
                        required=False, default=0, type=int)
    # --recreated developerTools\map_recreated.txt
    parser.add_argument("-r", "--recreated", help="choose document to save map template drawing",
                        required=False, default="developerTools\map_recreated.txt", type=str)
    # --template developerTools\map_template.txt
    parser.add_argument("-t", "--template", help="choose document to read map template drawing",
                        required=False, default="developerTools\map_template.txt", type=str)

    # args will be a dictionary containing the arguments
    args = vars(parser.parse_args())
    # init list of variables:
    # controller of script: True - generate map, false - recreate map from log
    control = args['control']
    # choose simulation log file
    simulation_log = args['document']
    # row of simulation log to recreate (used only if control is false)
    run_simulation = args['log']
    # file to save recreated map from simulation log
    map_recreated = args['recreated']
    # file to read map from drawing
    map_template = args['template']

    print("Args: Set control to %s" % args['control'])
    print("Args: Set document to %s" % args['document'])
    print("Args: Set log to %s" % args['log'])
    print("Args: Set recreated to %s" % args['recreated'])
    print("Args: Set template to %s" % args['template'])

    # set dictionary with symbols - can be changed if you wish to use other symbols instead
    symbols = {
        'W': 'Waiter',
        'T': 'Table',
        'F': 'Furnace',
        'X': 'Wall',
        '_': 'Blank'
    }
    print("RC: Executing Realm Controller for control %s, %s file, row %d:" % (control, simulation_log, run_simulation))
    if control:
        print("RC: Map generation executed...")
        # get map_template content
        lines = [line.rstrip('\n') for line in open(map_template)]
        # the longest row will be map size
        N = len(max(lines, key=len))
        waiter = []
        tables = []
        furnaces = []
        walls = []
        # parse file content to standard simulation log format
        for row in range(len(lines)):
            for i in range(len(lines[row])):
                coordinate = [i, row]
                dict_val = symbols[lines[row][i]]
                if dict_val == 'Waiter':
                    waiter.append(coordinate)
                if dict_val == 'Table':
                    tables.append(coordinate)
                if dict_val == 'Furnace':
                    furnaces.append(coordinate)
                if dict_val == 'Wall':
                    walls.append(coordinate)
        all_lists = [waiter, tables, furnaces, walls]
        # save state of simulation to file
        with open(simulation_log, "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t' + str(N) + '\t' + str(len(tables))
                         + '\t' + str(len(furnaces)) + '\t' + str(len(walls)) + '\t' + str(all_lists) + '\n')
        print("RC: Map recreated to file %s." % simulation_log)
        print("RC: Map generation complete.")
    else:
        print("RC: Map recreation executed...")
        # reload simulation state from log:
        # get last row in log
        with open(simulation_log) as myfile:
            log = list(myfile)[run_simulation].split('\t')
        myfile.close()
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
        # recreate simulation
        matrix = [['_' for _ in range(N)] for i in range(N)]
        # add agent
        matrix[coordinates[0][1]][coordinates[0][0]] = 'W'
        # counter counts number of used coordinates, so no object will occupy the same space in simulation
        counter = 1
        # add tables
        for i in range(num_tables):
            matrix[coordinates[i + counter][1]][coordinates[i + counter][0]] = 'T'
        # increase counter with number of used coordinates
        counter += num_tables
        # add furnaces
        for i in range(num_furnaces):
            matrix[coordinates[i + counter][1]][coordinates[i + counter][0]] = 'F'
        # increase counter with number of used coordinates
        counter += num_furnaces
        # add walls
        for i in range(num_walls):
            matrix[coordinates[i + counter][1]][coordinates[i + counter][0]] = 'X'
        # save state of simulation to file
        with open(map_recreated, "w") as myfile:
            for row in matrix:
                myfile.write(''.join(row) + '\n')
        myfile.close()
        print("RC: Map recreated to file %s." % map_recreated)
        print("RC: Map recreation complete.")

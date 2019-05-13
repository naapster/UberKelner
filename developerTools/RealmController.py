# map generating script

import datetime


if __name__ == '__main__':

    # controller of script: True - generate map, false - recreate map from log
    control = False
    # choose simulation log file
    simulation_log = "logs\simulation_log.txt"
    # row of simulation log to recreate (used only if control is false)
    run_simulation = 1

    # set dictionary with symbols - can be changed if you wish to use other symbols instead
    symbols = {
        'W': 'Waiter',
        'T': 'Table',
        'F': 'Furnace',
        'X': 'Wall',
        '_': 'Blank'
    }
    print("Executing RC for %s, row %d:" % (simulation_log, run_simulation))
    if control:
        print("Map generation executed...")
        # get map_template content
        lines = [line.rstrip('\n') for line in open('developerTools\map_template.txt')]
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
        print("Map generation complete.")
    else:
        print("Map recreation executed...")
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
        # recreate simulation
        matrix = [['_' for _ in range(N)] for i in range(N)]
        # add agent
        matrix[coordinates[0][0]][coordinates[0][1]] = 'W'
        # counter counts number of used coordinates, so no object will occupy the same space in simulation
        counter = 1
        # add tables
        for i in range(num_tables):
            matrix[coordinates[i + counter][0]][coordinates[i + counter][1]] = 'T'
        # increase counter with number of used coordinates
        counter += num_tables
        # add furnaces
        for i in range(num_furnaces):
            matrix[coordinates[i + counter][0]][coordinates[i + counter][1]] = 'F'
        # increase counter with number of used coordinates
        counter += num_furnaces
        # add walls
        for i in range(num_walls):
            matrix[coordinates[i + counter][0]][coordinates[i + counter][1]] = 'X'
        # save state of simulation to file
        with open("developerTools\map_recreated.txt", "w") as myfile:
            for row in matrix:
                myfile.write(''.join(row) + '\n')
        print("Map recreation complete.")

# map generating script

import datetime


if __name__ == '__main__':

    # get map_template content
    lines = [line.rstrip('\n') for line in open('map_template.txt')]

    # set dictionary with symbols - can be changed if you wish to use other symbols instead
    symbols = {
        'W': 'Waiter',
        'T': 'Table',
        'F': 'Furnace',
        'X': 'Wall',
        '_': 'Blank'
    }

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
    with open("simulation_log.txt", "a") as myfile:
        myfile.write(str(datetime.datetime.now()) + '\t' + str(N) + '\t' + str(len(tables))
                     + '\t' + str(len(furnaces)) + '\t' + str(len(walls)) + '\t' + str(all_lists) + '\n')

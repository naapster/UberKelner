
'''
UP    = [0, -1]
DOWN  = [0, 1]
RIGHT = [1, 0]
LEFT  = [-1, 0]
'''
solution_for_1 = [[1, 0], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [0, -1], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [0, 1], [0, 1], [-1, 0], [-1, 0], [1, 0], [0, -1], [0, -1], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [-1, 0], [-1, 0], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [0, -1], [0, -1],[1,0],[1,0],[-1,0],[0,-1],[-1,0],[-1,0],[-1,0],[-1,0],[0,-1],[0,-1],[0,-1],[0,-1],[1,0],[1,0],[1,0],[0,-1],[0,-1],[0,-1]]
solution_for_2 = [[1, 0], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [0, -1], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [-1, 0], [-1, 0], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [0, -1], [0, -1], [1, 0], [1, 0], [-1, 0],[0, -1], [-1, 0], [-1, 0], [-1, 0],[-1,0],[0,-1],[0,-1],[0,-1],[0,-1],[1,0],[1,0],[1,0],[0,-1],[0,-1],[0,-1]]
solution_for_3 = [[0, -1], [0, -1], [0, 1], [1, 0], [1, 0], [1, 0], [0, -1], [0, -1], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [-1, 0], [-1, 0], [0, -1], [-1, 0], [0, -1], [-1, 0], [-1, 0], [-1, 0], [0, -1], [0, -1], [1, 0], [0, -1], [-1, 0], [0, -1], [0, -1], [1, 0], [0, -1], [0, -1]]

# For last 2 from  /data/simulation_log.txt
with open('../documentation/test.txt') as f:
    lines = f.readlines()
    data3 = lines[0].replace('[', '').split('],')
    data2 = lines[1].replace('[', '').split('],')
    data1 = lines[2].replace('[', '').split('],')
    data_test3 = [list(map(int, s.replace(']', '').split(','))) for s in data3 ]
    data_test2 = [list(map(int, s.replace(']', '').split(','))) for s in data2]
    data_test1 = [list(map(int, s.replace(']', '').split(','))) for s in data1]

    print("TEST FOR 3 LAST MAP FROM /data/simulation_log.txt")

    print("Moves generated from UberKelner -3: " + str(data_test3))
    print("Movements that should happen:       " + str(solution_for_3))
    if solution_for_3 == data_test3:
        print("Test passed" + '\n')

    print("Moves generated from UberKelner -2: " + str(data_test2))
    print("Movements that should happen:       " + str(solution_for_2))
    if solution_for_2 == data_test2:
        print("Test passed" + '\n')

    print("Moves generated from UberKelner -1: " + str(data_test1))
    print("Movements that should happen:       " + str(solution_for_1))
    if solution_for_1 == data_test1:
        print("Test passed" + '\n')

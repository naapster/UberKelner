# scripts/__init__

all global variables used in project later + graphics init

# scripts/dinning_table

object containing information about tables in simulation - sprites, etc.

# scripts/furnace

object representing kitchen in simulation. Contains lists of ordered and ready dishes and coordinates of kitchen.

# scripts/matrix

Cartesian space N x N dimensional:

0,0 = 0,N
 
 ||....\\....||
 
N,0 = N,N


containing objects of simulation

# scripts/waiter

object serving as agent of simulation. Owns all the tables, kitchens and restaurant.

Can change his own coordinates in matrix by move_[direction] procedures and states of dinner tables (receive orders and give dishes). 

# main

main loop of simulation. Serves graphics window and simulation events, draws sprites basing on matrix values.

# simulation.log

text file containing simulation initializing state, used to recreate simulations.
Please note, that new logs are appending to the end of file.
# Developer log - todo list:

remake to_graph method: add furnaces and tables' coordinates to graph WITHOUT possibility of moving between two tables, two furnaces or furnace and table

remake DFS - list of lists of every possible path in graph, containing all tables and furnaces' coordinates
Best path is in subset containing path through coordinates of all furnaces and tables and is the shortest one



# Project structure and usage

## Project desription

Project code name: UberKelner

Project goal: to create a static discrete environment (hereinafter referred to as simulation) corresponding to
the real restaurant and the artificial intelligence agent serving as a waiter in the restaurant.

Agent, basing on available information about the simulation (we assume that the simulation is known and the agent has access
to the states of all objects inside the environment), chooses between movement actions or handling simulation objects.
At the beginning of the simulation, the restaurant is generated at any time of its activity - tables and kitchens
have randomly assigned states with which they start simulation. 

When one starts the game, part of the tables will be waiting for placing orders or taking out dishes. 
The waiter's task will be to set a strategy zeroing table states in the shortest possible time. 
The simulation ends when all tables are served and they will not have dishes to give, orders to place, or meals to receive.

PEAS specification:

• performance: the inverse of the time needed to zero the simulation

• environment: one state of the restaurant generated pseudorandomly from the seed or parameters taken from the log,
containing blank tiles, tables, furnaces, walls and waiter.

• actuators: waiter movement by one field vertically or horizontally, table service, kitchen service

• sensors: the agent has a tablet with the state of the restaurant.

The project consists of the following elements:

## images

contains all sprites used in project;

## scripts

contains all object scripts used in project:

### scripts/__init__

Legacy file - shows compiler where source files are

### scripts/dinning_table

Object containing information about tables in simulation - sprite, coordinates and state.

### scripts/furnace

Object containing information about furnaces in simulation - sprite, coordinates, time to prepare dish and lists of ordered dishes and prepared ones.

### scripts/matrix

Object representing environment of simulation. Contains matrix N*N with N set as parameter of simulation. 
Each coordinate in matrix responds to one object (either agent, furnace, table or wall).
The class has methods supporting processing data contained in it in accordance with the CRUD postulate 
(inserting, finding objects, modification and deletion of data).

Coordinates in Matrix cartesian space N x N dimensional:

0,0 = 0,N
 
 ||....\\....||
 
N,0 = N,N

Matrix can convert itself into graph, for artificial learning purpose.

### scripts/waiter

Object serving as agent of simulation. Owns all the tables, kitchens and restaurant.

Can change his own coordinates in matrix by move_[direction] procedures and states of dinner tables (receive orders and give dishes). 

The waiter has methods to move inside of simulation. The simulation supports the division into rounds - 
one round is the action of the waiter and subsequent changes of states of objects in the simulation.
The only action available is changing the position of the waiter in the matrix. 
Trying to enter table or kitchen causes automatic service of the object according to the priorities of the actions 
(taking the dishes, providing a meal, collecting the order). Priorities are available in the appendix to the project.

Waiter can calculate shortest path to the given destination point. 
Currently, the following methods of artificial learning are available:

* DFS

Calculation of path occures after pressing spacebar for the first time or after manual change of waiter coordinates through pressing arrows.
Pressing spacebar causes waiter to move to the next point of path. 
Pressing spacebar when waiter has reached his destination causes text information to appear in console.

### scripts/wall

object containing information about walls in simulation - sprite and coordinates.
Walls are simple representation of unreachable space.

## main

Main loop of simulation. Serves graphics window and simulation events, draws sprites basing on matrix values.
Allows to choose, which simulation should be loaded - random one or one from the simulation_log.

## map_template.txt

File containing map schema to be added by MapGenerator to simulation_log. 
Should contain only characters X, W, T, F, _, corresponding to wall, waiter, table, furnace and blank objects in simulation.
If user wishes to use other characters than these, dictionary of symbols in MapGenerator can be set up respectively.
Remember, maps are square and should contain the same number of characters in each line.

## MapGenerator

Script designed to convert map_template.txt contents into simulation_log.txt entry, in pursuance of the standard of simulation logs.

## simulation_log.txt

Text file containing simulation initializing state, used to recreate simulations.
Please note, that new logs are appending to the end of file.

All entries in this file have to obey the standard of simulation log:
> two fields for data \t number of elements in row (N) \t number of tables \t number of furnaces \t number of walls \t list of their coordinates

New logs can be added through:
* random generation of simulation in Main;
* map generation through translation of map_template.txt via MapGenerator;
* manually, injected directly into simulation_log

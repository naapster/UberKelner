# __init__

all global variables used in project later + graphics init

# matrix

Cartesian space N x N dimensional:

0,0 = 0,N
 
 ||....\\....||
 
N,0 = N,N


, containing information about state of in-game blocks:

0 - empty space

1 - waiter stands here

2 - empty dinner table

3+  kind of dish ordered to this place

# waiter

object serving as agent of simulation. Can change his own coordinates in matrix by move_[direction] procedures and states of dinner tables (receive orders and give dishes) 

# main

main loop of simulation. Serves graphics window and simulation events.
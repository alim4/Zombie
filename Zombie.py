__author__ = 'anthonylim'

#Asg8 outline

import random

SPACE = '  '
EMPTY = '.'
HEALTHY = 0 #occupied

'''
a number greater than zero represents a diseased
occupied space, with the number being the number of days that the
occupant has had the disease.
'''

def createEmptyGrid(cell_dim):
    ''' Creates an empty grid. '''

    grid = dict()
    for x in range(0, cell_dim):
        for y in range(0, cell_dim):
            grid[(x,y)] = EMPTY

    return grid

def initGrid(cell_dim, density, disease):
    ''' Returns a dictionary representation of our initial
        grid for simulation, using a 2-tuple key, e.g (x,y).
    '''

    '''
    1. Grid size

    This parameter is an integer that specifies the size of the grid.

    2. Population density

    This parameter is a number between 0 and 1
    which represents the probability that a square starts out occupied. To
    determine if a cell is occupied at the start, pick a random number
    between 0 and 1 (using random.random) and

    *make the cell occupied, if the random number is less than the density value.*

    Note that passing a 1 would mean ALL spaces start occupied. This parameter is only used
    during initial grid creation.

    3. Disease chance

    This is a number between 0 and 1 that represents the probability that an occupied square in the
    initial grid will be diseased. This parameter is only utilized during initial grid creation.
    '''

    grid = dict()
    for x in range(0, cell_dim):
        for y in range(0, cell_dim):
            rnd = random.random()
            if rnd < density:
                grid[(x,y)] = HEALTHY
            else:
                grid[(x,y)] = EMPTY
            # random.random() Return the next random floating point number in the range [0.0, 1.0).
            # https://docs.python.org/2/library/random.html#module-random
            # *make the cell occupied, if the random number is less than the density value.*

        #...
    return grid

def sim(grid_size, pop_density, disease, birth, spread, duration, mortality, days):
    ''' Function performs the simulation for the number of days specified. '''

    grid = initGrid(grid_size, pop_density, disease)

    #print your starting conditions before simulation
    printGrid(grid_size, grid, day=0)

    '''
    Days: This is a number greater than zero that specifies the number of days to simulate.
    '''

    for day in range(1, days+1):

        new_grid = createEmptyGrid(grid_size) #used for writing update sim results to

        '''
        The simulation works by computing the state of the grid at the end of
        the day based on the the state at the start of the day (the end of the
        previous day) and the following rules. The rules are applied to all of
        the cells simultaneously: all of the computations of a cell's new
        state are based on its state and that of its neighbors at the start of
        the day. Thus, it doesn't matter what order you compute cells' new
        states in, since all cells get their new values at the end of the day.
        '''

        # Iterate over today's grid cells and compute tomorrow's grid cell contents.
        #...


        '''
        After you've built up your new grid (the state of the simulation at
        the end of the day), you can copy it back to the current grid by using
        assignment (grid = new_grid). This is much faster than copying all of
        the key, value pairs. Yes, it's aliasing, but you don't need the old
        grid once you've used it to generate the new grid.
        '''

        grid = new_grid

	'''
        You must print your simulated grid after each simulated day, and the
        print out must be pretty. In other words, it must be an N x N grid of
        characters rather than one long string. You should print the day
        number above the grid.
        '''

        # print your grid
        printGrid(grid_size, grid, day)



def compute3x3Block(loc, grid, new_grid, birth_chance, spread_chance, disease_duration, mortality_rate):
    ''' Computes the next day's grid cells for 3 x 3 block of cells centered at loc. '''

    # Births / disease spread.
    # Two cases:
    # 1. Cells around cell @ loc are updated for *disease spread*
    # 2. Cell @ loc is updated depending on cells around it *birth chance*
    for x in range(loc[0]-1,loc[0]+2,1):
        for y in range(loc[1]-1,loc[1]+2,1):
            if (x,y) != loc: # only look at cells around center cell
                try:
                    '''
                    Birth chance:

                    This is a number between 0 and 1 and specifies the chance of an empty space becoming an occupied cell
                    given an adjacent occupied (and healthy) cell.

                    This probability is applied per-square; in other words,
                    if a square has four healthy neighbors (remember, an empty cell is neither healthy nor diseased),
                    it has four chances to become occupied itself.
                    '''

		    #...

                except:
                    pass # we're at a corner or edge

                try:
                    '''
                    Spread chance:

                    This is a number between 0 and 1 that represents the likelihood that the disease
                    will spread from one diseased square to its neighbors. The chance
                    applies separately to each neighbor, and could happen at any time that
                    the cell is sick. If a cell has four healthy neighbors, any number of
                    them (from 0 to 4) could become infected in a given turn.
                    '''

		    #...

                except:
                    pass # we're at a corner or edge

    '''
    Disease duration:

    This is the number of days that a cell remains diseased, from
    1 to 10. At the end of this duration, the occupant either dies or becomes
    healthy, as described below.

    Mortality rate:

    This is a number between 0
    and 1 that determines the chance that a diseased cell will die at the
    end of the disease duration. If the cell doesn't die at the end of the
    disease, it becomes healthy again.
    '''

    #Now, update the cell @ loc for the following...

    #Determine if cell location will die or recover.
    #OR..
    #Increment diseased cell days being sick.


def printGrid(cell_dim, grid, day):
    ''' Prints current grid line by line to standard out. '''

    print '\nDay: ' + str(day) + '\n'

    for x in range(0, cell_dim):
        for y in range(0, cell_dim):
            print grid.get((x,y)),
        print ""

def main():

    '''
    When run stand alone, your program must call your sim function with the
    following parameters: 20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 500
    '''

    sim(20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 2)


if __name__ == '__main__':
    main()
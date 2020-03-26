import random, time, copy
WIDTH = 50
HEIGHT = 10

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        r = random.randint(0,1)
        if r == 0:
            column.append(' ')
        else:
            column.append('#')
    nextCells.append(column)

while True:
    cells = copy.deepcopy(nextCells)
    print('\n\n\n\n\n') # Separate each step with newlines.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x][y], end='')
        print()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if cells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if cells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if cells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if cells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if cells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if cells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if cells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if cells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif cells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1)

        
        
        
            
        
        


    
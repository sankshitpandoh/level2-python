import random, time, copy
WIDTH = 10
HEIGHT = 10

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        r = random.randint(0,1)
        if r == 0:
            column.append('')
        else:
            column.append('#')
    nextCells.append(column)
    
# for i in range(WIDTH):
#     print(nextCells[i])

cells = copy.copy(nextCells)
while True:
    print('\n\n\n\n\n') # Separate each step with newlines.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x][y], end='')
        print()
    # print(y)

    for y in range(1,9):
        for x in range(1,9):
            if cells[x][y-1] == '#' and cells[x-1][y] == '#':
                cells[x][y]= '#'
            elif cells[x][y-1] == '#' and cells[x][y+1] == '#':
                cells[x][y]= '#'
            elif cells[x][y-1] == '#' and cells[x+1][y] == '#':
                cells[x][y]= '#'
            elif cells[x-1][y] == '#' and cells[x][y+1] == '#':
                cells[x][y]= '#'
            elif cells[x-1][y] == '#' and cells[x+1][y] == '#':
                cells[x][y]= '#'
            elif cells[x][y+1] == '#' and cells[x+1][y] == '#':
                cells[x][y]= '#'
            else:
                cells[x][y]=' '
    time.sleep(1)

        
        
        
            
        
        


    
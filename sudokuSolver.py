import math

#solve plugs in a number for the first non-filled cell based on a for loop
    #in the for loop, plug in 1, check conditions --> if they don't hold plug in
    #2, and so on until 9. If a number does work, call solve
    #If 9 doesn't work, return back up

def solve(grid, size):
    row = -1
    col = -1
    for i in range (0,len(grid)):
        for j in range (0,len(grid[0])):
            if grid[i][j] == 0:
                row = i
                col = j
                break
        if(row != -1):
            break

    if row == -1:
        return grid

    

    for i in range(1, size+1):
        grid[row][col] = i
        if checkConditions(grid) == True:
           solve(grid, size)
           if(isSolved(grid)):
               break
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                grid[row][col] = 0
                return grid


def checkConditions(grid):
    #rows
    for i in range (len(grid)):
        row = sorted(grid[i])
        for j in range (len(row)-1):
            if row[j] == row[j+1] and row[j]!=0:
                return False

    #cols
    for i in range (len(grid[0])):
        column = [0 for x in range(len(grid))]
        index = 0
        for j in range (len(grid)):
            column[index] = grid[j][i]
            index+=1
        column.sort()
        for j in range (len(column)-1):
            if column[j] == column[j+1] and column[j]!=0:
                return False

    #subcell
    sub = int(math.sqrt(len(grid)))
    subgrids = [[0 for rows in range(len(grid))] for cols in range(len(grid[0]))]
    
    outer = 0
    inner = 0

    #go through each row in grid. Assign it to the corresponding cell in subgrids
    
    for i in range (len(grid)):
        for j in range (len(grid[0])):
            subgrids[sub*int((i/sub))+int(j/sub)][sub*int((i%sub))+int(j%sub)] = grid[i][j]

    for i in range (len(subgrids)):
        subgrids[i].sort()
        for j in range (len(subgrids[i])-1):
            if subgrids[i][j] == subgrids[i][j+1] and subgrids[i][j]!=0:
                return False

    return True

def isSolved(grid):
    for i in range (len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 0):
                return False
    return True

size = 0
while (size!=4 and size!=9):
    size = int(input("Enter the size of the puzzle"))
grid = [[0 for rows in range(size)] for cols in range(size)]
print("Enter the values with no spaces in between each number, and use 0 for a blank cell.")
for i in range(size):
    typedRow = input("Enter row " + str(i+1) + ": ")
    k = 0
    for j in range (len(grid[0])):
        grid[i][j] = int(typedRow[k])
        k+=1

solve(grid, size)
for i in grid:
    print("".join(str(x) for x in i))

def pressedNum(grid, i, j):
    pn = grid[i][j]
    if(i >= 1):
        pn += grid[i-1][j]
    if(i + 1 < len(grid)):
        pn += grid[i+1][j]
    if(j >= 1):
        pn += grid[i][j-1]
    if(j + 1 < len(grid[0])):
        pn += grid[i][j+1]
    
    return pn

grid = []
for i in range(3):
    grid.append(list(map(int, input().split())))

# **list() or .copy() only works with list with no nested lists**
grid_new = [i[:] for i in grid]
for i in range(3):
    for j in range(3):
        num = pressedNum(grid, i, j)
        if((num % 2) == 0):
            grid_new[i][j] = 1
        else:
            grid_new[i][j] = 0
        
for i in grid_new:
    print("".join([str(s) for s in i]))

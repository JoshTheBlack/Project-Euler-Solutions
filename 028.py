# coding=utf-8
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
from comm import timed

def moveRight(x,y, grid, count):
    grid[y][x+1] = count
    return x+1, y, grid, count+1

def moveLeft(x,y, grid, count):
    grid[y][x-1] = count
    return x-1, y, grid, count+1

def moveUp(x,y, grid, count):
    grid[y-1][x] = count
    return x, y-1, grid, count+1

def moveDown(x,y, grid, count):
    grid[y+1][x] = count
    return x, y+1, grid, count+1

def even(x, y, grid, count, n):
    x, y, grid, count = moveLeft(x,y,grid,count)
    for j in range(1,n+1):
        x,y, grid, count = moveUp(x,y,grid,count)
    for j in range(1,n+1):
        x,y, grid, count = moveRight( x,y, grid, count)
    return x, y, grid, count, n+1

def odd(x, y, grid, count, n):
    x, y, grid, count = moveRight(x,y,grid,count)
    for j in range(1,n+1):
        x,y, grid, count = moveDown(x,y,grid,count)
    for j in range(1,n+1):
        x,y, grid, count = moveLeft( x,y, grid, count)
    return x, y, grid, count, n+1


def createSpiralGrid(sz):
    grid = [[0 for i in range(sz)] for j in range(sz)]
    n, count, x, y = 1, 2, sz // 2, sz // 2
    grid[y][x] = 1
    while count <= sz**2:
        if n % 2 == 0:
            x, y, grid, count, n = even(x, y, grid, count, n)
        else:
            x, y, grid, count, n = odd(x, y, grid, count, n)
    return grid

@timed
def sumGridDiagonals(sz):
    grid = createSpiralGrid(sz)
    sum = 0
    for i in range(len(grid)):
        sum += grid[i][i] + grid[len(grid)-1-i][i]
    return sum - grid[len(grid)//2][len(grid)//2]

print(sumGridDiagonals(1001))
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

def moveRight(x,y):
    return x+1, y

def moveLeft(x,y):
    return x-1, y

def moveUp(x,y):
    return x, y-1

def moveDown(x,y):
    return x, y+1

def createSpiralGrid(sz):
    grid = [[0 for i in range(sz)] for j in range(sz)]
    n = 1
    i = 2
    x = sz // 2
    y = x
    grid[y][x] = 1
    while i <= sz**2:
        if n % 2 == 0:
            x,y = moveLeft(x,y)
            grid[y][x] = i
            i += 1
            for j in range(1,n+1):
                x,y = moveUp(x,y)
                grid[y][x] = i
                i += 1
            for j in range(1,n+1):
                x,y = moveRight(x,y)
                grid[y][x] = i
                i += 1
            n += 1
        else:
            x,y = moveRight(x,y)
            grid[y][x] = i
            i += 1
            for j in range(1,n+1):
                x,y = moveDown(x,y)
                grid[y][x] = i
                i += 1
            for j in range(1,n+1):
                x,y = moveLeft(x,y)
                grid[y][x] = i
                i += 1
            n += 1
    return grid

@timed
def sumGridDiagonals(grid):
    sum = 0
    for i in range(len(grid)):
        sum += grid[i][i] + grid[len(grid)-1-i][i]
    return sum - grid[len(grid)//2][len(grid)//2]

print(sumGridDiagonals(createSpiralGrid(1001)))

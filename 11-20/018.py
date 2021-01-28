# coding=utf-8
from time import perf_counter
from functools import wraps
import os

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__}: {end-start:.6f} seconds")
        return result
    return wrapper

@timed
def path(tri, x):
    for i in range(x-1, -1, -1):
        for j in range(i+1):
            if tri[i+1][j] > tri[i+1][j+1]:
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]

    return tri[0][0]

# Open file for problem 67 and import data in to an array.
with open(os.path.join(os.sys.path[0],"67.txt"), "r") as ins:
    tmp = ins.read().split("\n")
    data = [i.split(" ") for i in tmp]

# Normalize the array to 100 columns by appending 0's
for i in range(len(data)):
    while len(data[i]) < 99:
        data[i].append(0)
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

grid = [[75,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [95,64,0,0,0,0,0,0,0,0,0,0,0,0,0], [17,47,82,0,0,0,0,0,0,0,0,0,0,0,0], [18,35,87,10,0,0,0,0,0,0,0,0,0,0,0], [20,4,82,47,65,0,0,0,0,0,0,0,0,0,0], [19,1,23,75,3,34,0,0,0,0,0,0,0,0,0], [88,2,77,73,7,63,67,0,0,0,0,0,0,0,0], [99,65,4,28,6,16,70,92,0,0,0,0,0,0,0], [41,41,26,56,83,40,80,70,33,0,0,0,0,0,0], [41,48,72,33,47,32,37,16,94,29,0,0,0,0,0], [53,71,44,65,25,43,91,52,97,51,14,0,0,0,0], [70,11,33,28,77,73,17,78,39,68,17,57,0,0,0], [91,71,52,38,17,14,91,43,58,50,27,29,48,0,0], [63,66,4,68,89,53,67,30,73,16,69,87,40,31,0], [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

print(path(grid, 14))
print(path(data, 99))
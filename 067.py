# coding=utf-8
# coding=utf-8
from comm import *

def path(tri, x):
    for i in range(x-1, -1, -1):
        for j in range(i+1):
            if tri[i+1][j] > tri[i+1][j+1]:
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]
    return tri[0][0]

@timed
def p67():
    import os
    data = []
    # Open file for problem 67 and import data in to an array.
    with open(os.path.join(os.sys.path[0],"67.txt"), "r") as ins:
        for line in ins:
            data.append([int(x) for x in line.strip().split(" ")])
    return path(data,99)

if __name__ == "__main__":
    print(p67())
# coding=utf-8
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.
from comm import *

@timed
def p62():
    x = 0
    cubes = []
    while True:
        x += 1
        cube = sorted(list(str(x**3)))
        cubes.append(cube)
        if cubes.count(cube) == 5:
            return (cubes.index(cube)+1)**3

print(p62())
# coding=utf-8
# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
from comm import *

@timed
def p48():
    x = 0
    for y in range(1,1001):
        x += y**y
    return str(x)[-10:]

@timed
def p48_2():
    return str(sum([i**i for i in range(1,1001)]))[-10:]

print(p48())
print(p48_2())
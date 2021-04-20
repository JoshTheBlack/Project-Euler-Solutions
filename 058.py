# coding=utf-8
from comm import *
from sympy import isprime

@timed
def p58(limit = 0.1):
    count, z = 0, 1
    x, y = 2, 1
    while True:
        for i in range(4):
            z += x
            if i == 3: continue
            if isprime(z): count += 1
        y += 2
        test = count / (2*y-1)
        if test < limit: return y        
        x += 2

print(p58())
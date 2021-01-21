# coding=utf-8
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
from math import sqrt
from sys import exit

t0 = time.time()

for a in range(1,500):
    for b in range(1,500):
        cSq = pow(a,2) + pow(b,2)
        c = sqrt(cSq)
        if c.is_integer() and a+b+int(c) == 1000:
            print(a*b*int(c))
            t1 = time.time()
            print(f"This calculation took {t1-t0} seconds")
            exit(0)
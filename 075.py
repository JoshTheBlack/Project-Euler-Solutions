# coding=utf-8
'''It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?'''
from comm import timed

DEBUG = False

@timed
def p075(max):
    def driver():
        from typing import DefaultDict
        from math import gcd
        limit = int((max/2)**0.5)
        triangles = DefaultDict(int)
        result = 0
        for m in range(2,limit):
            for n in range(1,m):
                if ((n+m) % 2) == 1 and gcd(n, m) == 1:
                    a = m**2 + n**2
                    b = m**2 - n**2
                    c = 2*m*n
                    p = a + b + c
                    while p < max:
                        triangles[p] += 1
                        if triangles[p] == 1: result += 1
                        if triangles[p] == 2: result -= 1
                        p += a+b+c
        return result
    
    return driver()

if __name__ == "__main__":
    print(p075(1_500_000))
# coding=utf-8
'''How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?'''
from comm import timed

@timed
def p073(max: int, a: int, b: int, x: int, y: int) -> int:
    '''max = set size, a = numerator of start, b = denominator of start
    c = numerator of end, d = denomenator of end; returns quantity of fractions
    between start and end'''
    c, d = nextFarey(max, a, b)
    result = 0
    while (c != x and d != y):
        result += 1
        z = (max + b) // d
        e = z * c - a
        f = z * d - b
        a = c
        b = d
        c = e
        d = f
    return result

def nextFarey(setSize: int, a: int, b: int) -> tuple:
    '''Finds the next ascending Farey Pair of a given set size.
    setSize = length of set, a = numerator of known pair, b = denominator of known pair'''
    for d in range(setSize,0,-1):
        if -(a*d)%b == 1:
            c = (1+a*d)//b
            return c,d

if __name__ == "__main__":
    print(p073(12_000, 1, 3, 1, 2))
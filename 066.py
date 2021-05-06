# coding=utf-8
# Consider quadratic Diophantine equations of the form:
# x2 – Dy2 = 1
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
from comm import *

@timed
def p66():
    result = []
    max = 0
    for d in range(2, 1001):
        limit = int(d**0.5)
        if d**0.5 == limit: continue
        m = 0
        dd = 1
        a = int(limit)
        n1 = 1
        n = a
        den1 = 0
        den = 1
        while (n**2 - d * den**2) != 1:
            m = dd * a - m
            dd = (d - m**2) / dd
            a = int((limit + m) / dd)
            n2 = n1
            n1 = n
            den2 = den1
            den1 = den
            n = a*n1+n2
            den = a*den1+den2
        if n > max:
            max = n
            result = d
    return result

print(p66())


# coding=utf-8
from comm import *
import sympy

def cf(n, max=10):
    fp = 42
    amount = 0
    ab = 10**-10
    while not abs(fp) <= ab and amount < max:
        integer = int(round(n, 10))
        fp = n - integer
        n = 1.0 / fp
        amount += 1
        yield integer

def convergents(n, max=10):
    n2ago = 0
    n1ago = 1
    d2ago = 1
    d1ago = 0
    for coef in cf(n, max=max+1):
        num = coef * n1ago + n2ago
        n2ago = n1ago
        n1ago = num
        den = coef * d1ago + d2ago
        d2ago = d1ago
        d1ago = den
        yield num, den

@timed
def p65():
    n = list(convergents(sympy.N(sympy.E, 120), 100))[99][0]
    print(sumDigits(n))

p65()
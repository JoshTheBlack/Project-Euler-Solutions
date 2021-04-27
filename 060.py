# coding=utf-8
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four 
# primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from operator import concat
from comm import *
from sympy import primerange, isprime

def catPrimeCheck(a,b):
    if isprime(int(str(a)+str(b))) and isprime(int(str(b)+str(a))):
            return True
    return False

@timed
def p60(range=10000):
    primes = list(primerange(1,range))
    for a in primes:
        if a == 2: continue
        for b in primes:
            if b <= a: continue
            if not catPrimeCheck(a,b): continue
            for c in primes:
                if c <= b or c <= a: continue
                if not catPrimeCheck(a,c): continue
                if not catPrimeCheck(b,c): continue
                for d in primes:
                    if d <= c or d <= b or d <= a: continue
                    if not catPrimeCheck(a,d): continue
                    if not catPrimeCheck(b,d): continue
                    if not catPrimeCheck(c,d): continue
                    for e in primes:
                        if e <= d or e <= c or e <= b or e <= a: continue
                        if not catPrimeCheck(a,e): continue
                        if not catPrimeCheck(b,e): continue
                        if not catPrimeCheck(c,e): continue
                        if not catPrimeCheck(d,e): continue
                        return f"{a+b+c+d+e} = {a} + {b} + {c} + {d} + {e}"
    p60(range*10)


p60()
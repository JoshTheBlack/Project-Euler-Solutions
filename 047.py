# coding=utf-8
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from comm import *

def findSequence(list):
    for x in range(len(list)-2):
        if sum(list[x:x+4]) == (4*list[x]+6):
                return x
    return False

@timed
def p47(n):
    primes = set(primeSieveRange(n))
    factors = dict([[x,[]] for x in range(2,n)])
    for item in factors.keys():
        if item in primes:
            factors[item] = [item]
        else:
            factors[item] = generateFactors(item,factors,[])
    fours = [item for item in factors.keys() if len(set(factors[item])) == 4]
    position = findSequence(fours)
    print(fours[position])

p47(200000)
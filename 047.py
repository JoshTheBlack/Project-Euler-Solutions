# coding=utf-8
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7 
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
# %% 
from comm import *
from itertools import combinations
from numpy import product

@timed
def p47():
    primes = primeSieveRange(150)
    test = combinations(primes,4)
    result = []
    for comb in test:
        x = product(comb)
        if x in result: continue
        result.append(product(comb))
    result = sorted(result)
    for number in result:
        if number + 1 not in result: continue
        if number + 2 not in result: continue
        if number + 3 not in result: continue
        return number

print(p47())

# %%

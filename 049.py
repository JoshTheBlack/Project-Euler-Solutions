# coding=utf-8
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
from comm import *


def isPerm(num,check):
    if len(str(num)) != len(str(check)) or num == check: return False
    for digit in str(num):
        if digit not in str(check): return False
        if str(check).count(digit) != str(num).count(digit): return False
    return True

def checkForPerms(lst):
    allPerms = []
    while len(lst) > 0:
        prime = lst[0]
        perms = [prime]
        for check in lst:
           if isPerm(prime,check): 
                perms.append(check)
        for rem in perms:
            lst.remove(rem)        
        if len(perms) > 1: allPerms.append(perms)
    return allPerms

@timed
def p49():
    perms = checkForPerms(primeSieveRange(1000,9999))
    results = []
    for perm in perms:
        if len(perm) < 3: continue
        length = len(perm)
        for x in perm:
            if x == 1487: continue
            for y in perm:
                if x > y: continue
                z = y - x
                if y + z in perm and y != x: return str(x) + str(y) + str(y+z)
    

print(p49())

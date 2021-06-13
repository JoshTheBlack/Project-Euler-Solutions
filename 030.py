# coding=utf-8
from comm import timed
from math import log10, floor

@timed
def sumPowers(power):
    count = 0
    for x in range(10, upperBoundary(power) + 1):
        if isNarcissistic(x,power):
            count += x
    return count

def isNarcissistic(n, power):
    return n == sum([ int(s)**power for s in str(n)])

def upperBoundary(power):
    n_digits = floor(log10(9**power)) + 1
    return n_digits * 9 ** power

if __name__ == "__main__":
    print(sumPowers(5))
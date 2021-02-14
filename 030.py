# coding=utf-8
from comm import timed

@timed
def sumPowers(power):
    count = 0
    for x in range(10,413345):
        if isNarcissistic(x,power):
            count += x
    return count

def isNarcissistic(n, power):
    return n == sum([ int(s)**power for s in str(n)])

print(sumPowers(5))
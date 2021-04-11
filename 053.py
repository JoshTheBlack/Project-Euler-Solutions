# coding=utf-8
from comm import *

def combinations(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

@timed
def p53():
    result = 0
    for n in range(101):
        for r in range(n+1):
            if combinations(n,r) > 1000000:
                result += 1
    return result

print(p53())
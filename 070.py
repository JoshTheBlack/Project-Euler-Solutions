# coding=utf-8
from comm import *

def isPermuted(x, y):
    return sorted(list(str(x))) == sorted(list(str(y)))

@timed
def p70():
    primes = primeSieveRange(10000)
    minRatio = 2
    bestN = 0
    for i in reversed(list(primes)):
        for j in primes:
            if j > i: continue
            n = i * j
            if n > 10 ** 7: continue
            phi = (i - 1) * (j - 1)
            ratio = n / phi
            if ratio < minRatio and isPermuted(n, phi):
                minRatio = ratio
                bestN = n
    return bestN

if __name__ == "__main__":
    print(p70())


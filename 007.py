# coding=utf-8
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from comm import primeSieveRange, timed
from sympy import sieve 

@timed
def p007(ind):
    '''Returns the indth prime number'''
    i = 110_000
    primes = primeSieveRange(1,i)
    while len(primes) < ind:
        i *= 2
        primes = primeSieveRange(1,i)
    return primes[ind-1]

if __name__ == "__main__":
    print(p007(10001))
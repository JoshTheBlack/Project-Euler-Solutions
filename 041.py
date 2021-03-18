# coding=utf-8
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 
# # 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
from comm import timed
import comm


@timed
def p41():
    # Generate a prime sieve of all primes below 100 million (Guessing at upper bound)
    primes = comm.primeSieveRange(7654321)
    # Check each prime number to see if it is pandigital, if so save it into a list called pdprimes.
    pdprimes = []
    for prime in primes:
        if comm.checkPandigital(prime):
            pdprimes.append(prime)
    # Sort the list of pandigital primes largest to smallest
    pdprimes = sorted(pdprimes,reverse=True)
    # Return the largest pandigital prime.
    return pdprimes[0]

print(p41())

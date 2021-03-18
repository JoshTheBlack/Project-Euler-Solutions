# coding=utf-8
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 
# # 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
from comm import timed
import comm
import itertools

def generatePandigitalNumbers(max=9):
    pandigitals = []
    digits = [1]
    for i in range(2,max+1):
        digits.append(i)
        for combination in itertools.permutations(digits):
            pandigitals.append(''.join(map(str, combination)))
    return pandigitals


@timed
def p41():
    # Generate a prime sieve of all primes below 7,654,321 (Guessing at upper bound)
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

@timed
def p41_2():
    # generate all pandigital numbers of length n where n < 9 and store it in a list ordered smallest to largest named pandigitals
    pandigitals = generatePandigitalNumbers(9) 
    # check each number in pandigitals for primality.  If prime, store it in result.
    for number in pandigitals:
        if comm.is_prime(int(number)):
            result = number
    return result


#print(p41())
print(p41_2())

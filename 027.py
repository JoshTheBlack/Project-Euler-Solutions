# coding=utf-8
# Find the product of the coefficients, a and b, for the quadratic expression that produces
# the maximum nuber of primes for consecutive values of n, starting with n = 0.
from comm import timed
import comm

def findNumberOfQuadraticPrimes(a,b):
    count = 0
    stop = False
    while stop == False:
        for n in range(1000):
            if comm.is_prime((n**2 + (a*n) + b)) == True:
                count += 1
            else:
                stop == True
                return count

@timed
def findLargestNumberOfQuadraticPrimes(n):
    results = {}
    results[0] = [0,0]
    for a in range(-n,n+1):
        for b in range(-n,n+1):
            number = findNumberOfQuadraticPrimes(a,b)
            if number > max(results):
                results[number] = [a,b]
    return results[max(results)][0] * results[max(results)][1]

print(findLargestNumberOfQuadraticPrimes(1000))
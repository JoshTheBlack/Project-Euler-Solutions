# coding=utf-8
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from comm import *

def truncatablePrimeTest(number):
    for i in range(1,len(str(number))+1):
        if not is_prime(int(str(number)[:i])):
            return False
        if not is_prime(int(str(number)[-i:])):
            return False
    return True

@timed
def driver(primeArray):
    del primeArray[0:4]
    count, answer = 0, 0
    for prime in primeArray:
        if truncatablePrimeTest(prime):
            answer += prime
            count += 1
            if count == 11:
                break
    return answer

if __name__ == "__main__":
    print(driver(primeArray = primeSieveRange(1000000)))
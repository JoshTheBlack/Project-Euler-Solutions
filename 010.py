# coding=utf-8
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from comm import timed, primeSieveRange

@timed
def p010(max = 2_000_000):
    primes = primeSieveRange(max)
    return sum(primes)

if __name__ == "__main__":
    print(p010())
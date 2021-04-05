# coding=utf-8
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from comm import *

@timed
def p50():
    primes = primeSieveRange(1000000)
    result = []
    best = 0
    for i in range(4):
        firstPrime = primes[i]
        primePosition = primes.index(firstPrime)
        primeSum = firstPrime
        count = 1
        while True:
            primePosition += 1
            if primePosition >= len(primes): 
                result.append([primeSum, firstPrime, count])
                break
            primeSum += primes[primePosition]
            if primeSum > 1000000: break
            count += 1
            if primeSum in primes and count > best: 
                best = count
                result.append([primeSum, firstPrime, count])
                continue
    result = sorted(result, reverse=True)[0]
    return f"{result[0]} is the prime sum of the longest string of consecutive primes starting with {result[1]} and summing through {result[2]} consecutive primes."

def maxPrimeSum(max):
    primes = primeSieveRange(max)
    sum = 0
    pos = -1
    count = 0
    while sum < max:
        pos += 1
        sum += primes[pos]
    while True:
        if sum > max:
            sum -= primes[pos]
        if sum - primes[count] in primes: yield sum - primes[count]
        sum -= primes[count]
        count += 1

@timed
def p50_2(max):
    result = maxPrimeSum(max)
    return next(result)


print(p50())

print(p50_2(1000000))


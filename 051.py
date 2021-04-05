# coding=utf-8
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes 
# among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
# being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.
from comm import *

def digitReplacement(orig, places):
    result = []
    for x in range(10):
        number = str(orig)
        count = 0
        newNumber = ""
        for digit in number:
            if count in places: newNumber += str(x)
            if count not in places: newNumber += digit
            count += 1
        result.append(int(newNumber))
    return result

def primesWithRepeatedDigitsSearch(primes):
    repeatedDigitsQuantity = [3,5,6,7,8,9]
    for prime in primes:
        import collections
        d = collections.defaultdict(int)
        for c in str(prime):
            d[c] += 1
        for c in sorted(d, key=d.get, reverse=True):
            if d[c] in repeatedDigitsQuantity: 
                places = []
                count = 0
                for digit in str(prime):
                    if digit == c:
                        places.append(count)
                    count += 1
                yield prime, places

@timed
def p51():
    primes = primeSieveRange(10,1000000)
    nextPrime = primesWithRepeatedDigitsSearch(primes)
    while True:
        prime, position = next(nextPrime)
        test = digitReplacement(prime, position)
        count = 0
        for number in test:
            if len(str(number)) != len(str(prime)): continue
            if is_prime(number): count += 1
            if count == 8:
                for result in test:
                    if len(str(result)) != len(str(prime)): continue
                    if not is_prime(result): continue
                    return result

# def p51():
#     x = primeSet()
#     while True:
#         print(next(x))

print(p51())
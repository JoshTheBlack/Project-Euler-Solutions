# coding=utf-8
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
from comm import *

@timed
def p35(limit):
    primeArray = set(primes(limit))
    circularPrimeArray = [2,5]
    avoid = [2,4,5,6,8,0]
    for i in range(1,limit):
        if i not in circularPrimeArray and i in primeArray:
            run = True
            while run == True:
                for num in str(i):
                    if int(num) in avoid:
                        run = False
                if run == False:
                    break
                x = rotateDigits(i)
                for number in x:
                    if number not in primeArray:
                        run = False
                        break
                if run == False:
                    break
                for number in x:
                    circularPrimeArray.append(number)
                    run = False
    return len(circularPrimeArray)

print(p35(1000000))
# coding=utf-8
# Pandigital Multiples
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
from comm import timed

def concatenateNumbers(numArray):
    result = ''
    for arg in numArray:
        result += str(arg)
    return int(result)

def checkPandigital(number):
    digits = []
    for letter in str(number):
        digits.append(int(letter))
    if set(digits) == set(range(1,10)):
        return True
    else:
        return False

def buildPMultiples(number):
    length = 0
    result = []
    for i in range(1,10):
        x = number * i
        length += len(str(x))
        result.append(x)
        if length > 9:
            return False
        if length == 9:
            return result

@timed
def p38():
    result = []
    for i in range(9123,10000):
        pMs = buildPMultiples(i)
        if pMs != False:
            x = concatenateNumbers(pMs)
            if checkPandigital(x):
                result.append(x)
    return sorted(result,reverse=True)[0]

print(p38())

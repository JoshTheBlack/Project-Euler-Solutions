# coding=utf-8
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
from comm import *

def buildFactorialDict():
    dict = {}
    for dig in range(0,10):
        dict[dig] = factorial(dig)
    return dict

def checkCurious2(number):
    x = 0
    for num in str(number):
        x += factorial(int(num))
    if x == number:
        return True
    else:
        return False

def checkCurious(number,dict):
    x = 0
    for num in str(number):
        x += dict[int(num)]
    if x == number:
        return True
    else:
        return False

@timed
def driver():
    dict = buildFactorialDict()
    x = 0
    for n in range(3,999999):
        if checkCurious(n,dict):
            x += n
    return x

print(driver())
#print(6*factorial(9))

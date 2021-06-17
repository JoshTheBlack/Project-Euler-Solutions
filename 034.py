# coding=utf-8
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
from comm import *

def buildFactorialArray():
    facts = []
    for dig in range(0,10):
        facts.append(factorial(dig))
    return facts

def checkCurious(number,facts): # number to check and array of factorials 0 - 9
    x = 0
    for num in str(number):
        x += facts[int(num)]
    if x == number:
        return True
    else:
        return False

@timed
def driver():
    facts = buildFactorialArray()
    x = 0
    for n in range(3,999_999):
        if checkCurious(n,facts):
            x += n
    return x

if __name__ == "__main__":
    print(driver())
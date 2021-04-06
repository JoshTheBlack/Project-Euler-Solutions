# coding=utf-8
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from comm import *

def hasSameDigits(num1, num2):
    l1, l2 = [], []
    l1.extend(str(num1))
    l2.extend(str(num2))
    if sorted(l1) == sorted(l2):
        return True
    return False

@timed
def p52():
    num = 1
    multiplier = 2
    while True:
        test = num * multiplier
        if hasSameDigits(num,test):
            if multiplier == 6:
                return num
            multiplier += 1
            continue
        multiplier = 2
        num += 1

if __name__ == '__main__': 
    print(p52())
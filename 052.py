# coding=utf-8
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from comm import *

def hasSameDigits(num1, num2):
    if sorted(str(num1)) == sorted(str(num2)):
        return True
    return False

def recTest(num,mul = 2):
    num2 = num * mul
    if hasSameDigits(num,num2):
        if mul == 6: return num
        return recTest(num,mul+1)
    return False

@timed
def main():
    num = 1
    while not recTest(num):
        num += 1
    return num

if __name__ == '__main__': 
    print(main())
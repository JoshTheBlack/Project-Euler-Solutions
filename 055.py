# coding=utf-8
# How many Lychrel numbers are there below ten-thousand?
# Assume that all numbers are Lychrel until proven otherwise.
# Assume that a number is non-Lychrel if you reach a palindromic number within 50 iterations.
from comm import *

@timed
def p55(max=10000):
    result = 0
    for i in range(max):
        x = i
        for j in range(51):
            y = reverseNumber(x)
            if isPalindrome(x+y): break
            if j == 50: result += 1
            x = x+y
    return result

if __name__ == "__main__":
    print(p55())

        

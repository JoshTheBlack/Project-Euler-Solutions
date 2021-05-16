# coding=utf-8
# The sum of the squares of the first ten natural numbers is 385 (1sq + 2sq ... +10sq)
# The square of the sum of the first ten natural numbers is 3025 (1+2+3..+10)squared = 55sq = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from comm import timed

def squareSum(arr):
    result = 0
    for num in arr:
        result += num
    return result ** 2

def sumSquare(arr):
    result = 0
    for num in arr:
        result += num ** 2
    return result
    
@timed
def p006(max = 100):
    nums = [i for i in range(max+1)]
    return squareSum(nums) - sumSquare(nums)

if __name__ == "__main__":
    print(p006())
# coding=utf-8
# Find the sum of the digits in the number 100!
from comm import timed, factorial, sumDigits

@timed
def driver(n):
    x = factorial(n)
    y = sumDigits(x)
    return y

if __name__ == "__main__":
    print(driver(100))
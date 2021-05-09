# coding=utf-8
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from comm import timed, sumDigits

def remainderFree(x):
        for num in range(2,21,1):
            if x % num != 0:
                return False
        return True

@timed
def driver():
    x = 20
    while True:
        x += 20
        if remainderFree(x): return x

print(driver())
# coding=utf-8
# Find the sum of the digits in the number 100!
import comm as comm
from comm import timed

@timed
def driver(n):
    x = comm.factorial(n)
    y = comm.sumDigits(x)
    return y

print(driver(100))
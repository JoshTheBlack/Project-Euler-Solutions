# coding=utf-8
# Find the sum of the digits in the number 100!
import Completed.comm as comm
from Completed.comm import timed
from functools import wraps


@timed
def driver(n):
    x = comm.factorial(n)
    y = comm.sumDigits(x)
    return y

print(driver(100))
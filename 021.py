# coding=utf-8
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
import comm
from comm import timed
from functools import wraps

def isAmicable(n):
    x = sum(comm.factors(n), -n)
    y = sum(comm.factors(x), -x)
    if y == n and y != x:
        return True
    else:
        return False

@timed
def driver():
    result = 0
    for i in range(2, 10001):
        if isAmicable(i) == True:
            result += i
    return result

print(driver())
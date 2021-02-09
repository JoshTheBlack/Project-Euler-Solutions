# coding=utf-8
import comm
from comm import timed

@timed
def driver():
    abundantSet = set(i for i in range(1,30000) if comm.sumProperDivisors(i) > i)
    summedSet = set(x+y for x in abundantSet for y in abundantSet)
    return sum(set(range(1,28124)) - summedSet)

print(driver())
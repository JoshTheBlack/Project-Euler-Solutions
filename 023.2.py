# coding=utf-8
from comm import timed, sumProperDivisors

@timed
def driver():
    abundantSet = set(i for i in range(1,28124) if sumProperDivisors(i) > i)
    summedSet = set(x+y for x in abundantSet for y in abundantSet)
    return sum(set(range(1,28124)) - summedSet)

if __name__ == "__main__":
    print(driver())
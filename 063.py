# coding=utf-8
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
from comm import *

def countPower(power):
    x = 0
    count = 0
    while True:
        x += 1
        pow = x ** power
        if len(str(pow)) == power: count += 1
        if len(str(pow)) > power: return count

@timed
def p63():
    count = 0
    for i in range(99):
        count += countPower(i)
    return count

if __name__ == "__main__":
    print(p63())
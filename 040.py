# coding=utf-8
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from comm import timed

def buildFraction(length):
    l = 0
    x = 1
    fraction = "."
    while l < length+1:
        fraction += str(x)
        x += 1
        l = len(fraction)
    return fraction

def d(index, fraction):
    return int(fraction[index])

@timed
def p40():
    fraction = buildFraction(1000000)
    return d(1,fraction) * d(10,fraction) * d(100,fraction) * d(1000,fraction) * d(10000,fraction) * d(100000,fraction) * d(1000000,fraction)

if __name__ == "__main__":
    print(p40())

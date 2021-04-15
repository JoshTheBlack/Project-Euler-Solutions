# coding=utf-8
# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
from comm import *

@timed
def p56(max=100):
    result = 0
    for a in range(100):
        for b in range(100):
            if sumDigits(a**b) > result: result = sumDigits(a**b)
    return result

if __name__ == "__main__":
    print(p56())
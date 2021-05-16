# coding=utf-8
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from comm import timed

@timed
def p009():
    for a in range(1,500):
        for b in range(1,500):
            c = (a**2 + b**2)**0.5
            if c == int(c) and a + b + c == 1000:
                return a * b * int(c)

if __name__ == "__main__":
    print(p009())
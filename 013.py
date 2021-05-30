# coding=utf-8
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (in 13.txt)
from comm import timed
import os
import numpy as np

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), skiprows=0, delimiter=" "))

@timed
def p013(data):
    total = 0

    for i in data:
        total += int(i)

    return str(total)[0:10]

if __name__ == "__main__":
    print(p013(importData("13.txt")))
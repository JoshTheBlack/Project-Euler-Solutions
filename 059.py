# coding=utf-8
# Decrypt an XOR encrypted message that has a key of 3 lower-case characters.
from comm import *
import numpy as np
import os

def importData():
    data = np.loadtxt(os.path.join(os.sys.path[0], "p059_cipher.txt"), dtype=str, skiprows=0, delimiter=",")
    return data

def decryptXor(data,key):
    result = []
    for i in range(len(data)):
        result.append(int(data[i]) ^ key[i%len(key)])
    return result

def keyGenerator():
    for a in range(97,123):
        for b in range(122,96,-1):
            for c in range(122,96,-1):
                yield [a,b,c]

@timed
def p59():
    keyGen = keyGenerator()
    data = importData()
    while True:
        key = next(keyGen)
        test = convertToAscii(decryptXor(data,key))
        if "and" in test and "=" not in test and "*" not in test:
            print(test)
            print(sum(decryptXor(data,key)))
            print(convertToAscii(key))
            break

p59()
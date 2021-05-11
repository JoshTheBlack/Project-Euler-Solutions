# coding=utf-8
from comm import timed
import itertools

def validate(data, vsum):
    if data[0] + data[1] + data[2] != vsum: return False
    if data[3] + data[2] + data[4] != vsum: return False
    if data[5] + data[4] + data[6] != vsum: return False
    if data[7] + data[6] + data[8] != vsum: return False
    if data[9] + data[8] + data[1] != vsum: return False
    return True

def find(vsum):
    a = itertools.permutations(range(1,11))
    while True:
        x = next(a)
        if validate(x, vsum):
            yield x

@timed
def p68(vsum = 14):
    max = 0
    a = list(find(vsum))
    print(len(a))
    for li in a:
        n1 = str(li[0]) + str(li[1]) + str(li[2]) 
        n2 = str(li[3]) + str(li[2]) + str(li[4])
        n3 = str(li[5]) + str(li[4]) + str(li[6])
        n4 = str(li[7]) + str(li[6]) + str(li[8])
        n5 = str(li[9]) + str(li[8]) + str(li[1])
        test = min([li[0], li[3], li[5], li[7], li[9]])
        if li[0] == test:
            result = n1 + n2 + n3 + n4 + n5
        if li[3] == test:
            result = n2 + n3 + n4 + n5 + n1
        if li[5] == test:
            result = n3 + n4 + n5 + n1 + n2
        if li[7] == test:
            result = n4 + n5 + n1 + n2 + n3
        if li[9] == test:
            result = n5 + n1 + n2 + n3 + n4
        if len(result) == 16 and int(result) > max:
            max = int(result)
    return max

print(p68())

# coding = utf-8
from comm import *
import sys, math

sys.setrecursionlimit(3500)

@timed
def p57(num=3, den=2, count=0, max=1000, result=0):
    while count <= max:
        num,den = num+2*den, num+den
        count += 1
        if int(math.log10(num)) > int(math.log10(den)):
            result += 1
        if count == max: return result

def cf(num,den,count=0,max=1000,result=0):
        num,den = num+2*den, num+den
        count += 1
        if int(math.log10(num)) > int(math.log10(den)): result += 1
        if count >= max: 
            return result
        return cf(num,den,count,max,result)

@timed
def p57_2(max=1000):
    result = cf(3,2,max=max)

@timed
def p57_3(max=1000):
    return math.floor(max/13*2)

print(p57())
print(p57_2())
print(p57_3())
# coding = utf-8
from comm import *

@timed
def p57(num=3, den=2, count=0, max=1000, result=0):
    while count <= max:
        num,den = num+2*den, num+den
        count += 1
        if len(str(num)) > len(str(den)):
            result += 1
        if count == max: return result

print(p57())
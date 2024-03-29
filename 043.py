# coding=utf-8
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
import comm
from comm import timed
import itertools

@timed 
def generateAllPandigitalNumbersRange(min=1,max=9,length=0):
    pandigitals = []
    digits = [min] if length == 0 else [i for i in range(min,min+length)]
    if length != 0:
        for combination in itertools.permutations(digits):
                pandigitals.append(int(''.join(map(str, combination))))
    else:
        for i in range(min+1,max+1):
            digits.append(i)
            for combination in itertools.permutations(digits):
                pandigitals.append(int(''.join(map(str, combination))))
    return pandigitals

def isPrimeSubDivisible(number):
    if int(str(number)[5:8]) % 11 != 0:
        return False
    if int(str(number)[7:10]) % 17 != 0:
        return False
    if int(str(number)[6:9]) % 13 != 0:
        return False
    if int(str(number)[3:4]) not in [0,2,4,6,8]:
        return False
    if int(str(number)[2:5]) % 3 != 0:
        return False    
    if int(str(number)[5:6]) not in [0,5]:
        return False
    if int(str(number)[4:7]) % 7 != 0:
        return False
    return True

# First attempt code, brute-force.  Slow.
@timed
def p43(pandigital10):
    sum = 0
    for number in pandigital10:
        if isPrimeSubDivisible(str(number)):
            sum += number
    return sum

def rem(x,y):
    return [i for i in x if i not in y]

#Second attempt, generate and eliminate along the way.  Faster
@timed
def p43_2():
    digits = "0123456789"
    answer = []
    for a in digits:
        for b in rem(digits,a):
            for c in rem(digits,a+b):
                for d in rem(digits,a+b+c):
                    if (int(b+c+d) % 2 != 0): continue
                    for e in rem(digits,a+b+c+d):
                        if (int(c+d+e) % 3 != 0): continue
                        for f in rem(digits,a+b+c+d+e):
                            if (int(d+e+f) % 5 != 0): continue
                            for g in rem(digits,a+b+c+d+e+f):
                                if (int(e+f+g) % 7 != 0): continue
                                for h in rem(digits,a+b+c+d+e+f+g):
                                    if (int(f+g+h) % 11 != 0): continue
                                    for i in rem(digits,a+b+c+d+e+f+g+h):
                                        if (int(g+h+i) % 13 != 0): continue
                                        for j in rem(digits,a+b+c+d+e+f+g+h+i):
                                            if (int(h+i+j) % 17 == 0):
                                                answer.append(int(a+b+c+d+e+f+g+h+i+j))
    return f"Found {len(answer)} matching numbers summing to {sum(answer)}"

def unique(number):
    for digit in str(number):
        if str(number).count(digit) != 1:
            return False
    return True

# Third attempt, build the number backwards for efficiency.  (There are less numbers divisible by 17 than 2.)  Roughy 80 times faster.
@timed
def p43_3():
    digits = "0123456789"
    answer = []
    for hij in range(17,1000,17):
        if not unique(hij): continue
        if len(str(hij)) == 2: hij = "0" + str(hij)
        for g in rem(digits,str(hij)):
            if int(g+str(hij)[:-1]) % 13 != 0: continue
            for f in rem(digits,g+str(hij)):
                if int(f+g+str(hij)[:-2]) % 11 != 0: continue
                for e in rem(digits,f+g+str(hij)):
                    if int(e+f+g) % 7 !=0: continue
                    for d in rem(digits,e+f+g+str(hij)):
                        if int(d+e+f) % 5 !=0: continue
                        for c in rem(digits,d+e+f+g+str(hij)):
                            if int(c+d+e) % 3 != 0 : continue
                            for b in rem(digits,c+d+e+f+g+str(hij)):
                                if int(b+c+d) % 2 != 0: continue
                                answer.append(int(rem(digits,b+c+d+e+f+g+str(hij))[0]+b+c+d+e+f+g+str(hij)))
    return f"Found {len(answer)} matching numbers totalling {sum(answer)}"

if __name__ == "__main__":
    print(p43_3())
    print(p43_2())
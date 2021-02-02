# coding=utf-8
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def remainderFree(x):
    isTrue = True
    while isTrue == True:
        for numbers in range(2,21,1):
            if x % numbers != 0:
                isTrue = False
                break
        return(isTrue)

stop = False
y = 0
while stop == False:
    y += 20
    stop = remainderFree(y)

print(y)
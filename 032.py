# coding=utf-8
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
from comm import timed
import comm

def isUnusual(number):
    factors = comm.orderedFactors(number) # function to return a 2d array of factor pairs
    for i in range(0,len(factors)):
        string = "".join(sorted(str(number) + str(factors[i][0]) + str(factors[i][1]))) # create ordered string of factor pair and number
        if string == "123456789":
            return True
    return False

@timed
def sumUnusualProducts():
    answer = 0
    for i in range(1000,10000):
        if isUnusual(i):
            answer += i
    return answer

print(sumUnusualProducts())
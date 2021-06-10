# coding=utf-8
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as 
# the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from comm import timed, factors

def find_abundant_numbers():
    abundant = []
    for number in range(1,21823):
        if sum(factors(number),-number) > number:
            abundant.append(number)
    return abundant

def findPair(A, sum):  # Find if any two values in array "A" can add up to the sum "sum"
    dict = {}
    for i, e in enumerate(A):
        if sum - e in dict or sum // 2 in dict and sum in dict:
            return True
        dict[e] = i # Store current enumerated element in the dictionary.
    return False

@timed
def driver():
    answer = []
    abundant = find_abundant_numbers()
    for number in range(1,21823):
        if not findPair(abundant, number):
            answer.append(number)
    return sum(answer)

if __name__ == "__main__":
    print(driver())
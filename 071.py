# coding=utf-8
'''Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7. '''
from comm import timed

'''Farey Neighbors can be calculated where numless / denless < nummore /denmore
using the formula denmore*numless - nummore*denless = 1'''
@timed
def p71(max, nr = 3, dr = 7):
    # Start search for next denominator in series by counting back from max.
    for dl in range(max, 0, -1):
        if dl*nr%dr == 1: break # If denless * nummore / denmore has a remainder of 1, you've found the neighbor denominator
    return (dl*nr-1)//dr # Use algebra to calculate numerator as answer to question
    

if __name__ == "__main__":
    print(p71(1_000_000))

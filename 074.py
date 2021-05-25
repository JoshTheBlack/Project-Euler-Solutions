# coding=utf-8
''' The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?'''
from comm import timed

DEBUG = False

@timed
def p074(n):
    facts = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
    chainLengths = {169:3,363601:3,1454:3,871:2,45361:2,872:2,45362:2}
    amountOfLen60 = 0
    
    def chainLength(num):
        if num not in chainLengths:
            sumFacts = sum([facts[x] for x in str(num)])
            if sumFacts == num: 
                chainLengths[num] = 1
            else: 
                chainLengths[num] = 1 + chainLength(sumFacts)
        return chainLengths[num]

    for i in range(n):
        if chainLength(i) == 60:
            if DEBUG: print(f"Found {i} has a chain length of 60.")
            amountOfLen60 += 1
    return amountOfLen60

if __name__ == "__main__":
    print(p074(1_000_000))

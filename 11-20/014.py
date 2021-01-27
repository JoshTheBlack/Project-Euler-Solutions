# coding=utf-8
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
import time

def collatz(s):
    t = s
    count = 1
    #num = [s]
    while s != 1:
        if s < t:
            count += ans[s-1][0] - 1
            return count, t#, num
        elif s % 2 == 0:
            s //= 2
            count += 1
        else:
            s = 3 * s + 1
            count += 1
    return count, t #, num

t0 = time.time()
ans = []
for i in range(1, 1000000):
    ans.append(collatz(i))
ans.sort(reverse=True)
print(f"The number {ans[0][1]} took {ans[0][0]} hops to 1.")

t1 = time.time()
print(f"This calculation took {t1-t0} seconds.") # Display time elapsed during calculation.
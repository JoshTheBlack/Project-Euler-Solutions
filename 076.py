# coding=utf-8
'''It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?'''
from comm import timed

def p(num, computed = {0:1}):
    if num in computed: return computed[num]
    total = 0
    for k in range(1, num+1):
        total += pow(-1, k+1) * (p(num - k*(3*k-1)//2, computed) + p(num - k*(3*k+1)//2, computed))
    computed[num] = total
    return total

@timed
def P(target = 100):
    ways = [0 for i in range(target+1)]
    ways[0] = 1
    for i in range(1, 100):
        for j in range(i, target+1):
            ways[j] += ways[j-i]
    return ways[target]

@timed
def p076(n):
    return p(n) - 1

if __name__ == "__main__":
    print(p076(100))
    print(P())

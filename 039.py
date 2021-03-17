# coding=utf-8
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
from comm import timed
from math import sqrt

def findABC(p):
    result = []
    for a in range(1,p//2):
        for b in range(a,p//2):
            c = sqrt(a**2 + b**2)
            if a + b + int(c) == p and c % 1 == 0:
                result.append(sorted([a,b,int(c)]))
    final = []
    for solution in result:
        if solution not in final:
            final.append(solution)
    return final

@timed
def p39():
    answer = []
    for i in range(1001):
        x = findABC(i)
        if len(x) > len(answer):
            answer = x
    return sum(answer[0]), answer


from math import sqrt, ceil
@timed
def test():
    max_solutions = 0

    cpmaxratio = (2 + sqrt(2))/sqrt(2)

    for p in range(1000):
        solutions = 0
        for c in range(int(p / cpmaxratio), int(ceil(p / 2.))):
            try:
                b = int(abs(sqrt(c * c + 2 * c * p - p * p) - c + p) / 2)
            except:
                b = 0
            if b != 0 and (p - c - b) ** 2 + b * b == c * c:
            	solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            best_p = p

    print(best_p, max_solutions)

test()
print(p39())
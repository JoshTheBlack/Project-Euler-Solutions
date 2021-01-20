# coding=utf-8
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    x = str(x)
    y = ''.join(reversed(str(x)))
    if x == y:
        return True
    else:
        return False

solutionFound = False
answer = []
for n in range(999,10,-1):
    for i in range(999,10,-1):
        test = is_palindrome(n*i)
        if test == True:
            answer.append(n * i)

print(max(answer))
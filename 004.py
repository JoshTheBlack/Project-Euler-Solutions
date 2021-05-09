# coding=utf-8
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from comm import isPalindrome, timed

@timed
def p004():
    answer = []
    for n in range(999,10,-1):
        for i in range(999,10,-1):
            x = n * i
            if isPalindrome(x):
                answer.append(x)
    return max(answer)

if __name__ == "__main__":
    print(p004())
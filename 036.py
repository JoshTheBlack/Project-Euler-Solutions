# coding=utf-8
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
from comm import *

def is_palindrome(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        return True
    else:
        return False

def build_decimal_palindromes(max):
    decimalPalindromes = []
    for i in range(1,max):
        if is_palindrome(i):
            decimalPalindromes.append(i)
    return decimalPalindromes

@timed
def driver():
    decimalPalindromes = build_decimal_palindromes(1000000)
    answer = 0
    for num in decimalPalindromes:
        if is_palindrome(int(bin(num).replace("0b",""))):
            answer += num
    return answer

print(driver())
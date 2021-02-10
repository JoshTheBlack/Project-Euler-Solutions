# coding=utf-8
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import comm
from comm import timed

@timed
def fibbonacciLengthIndex(n):
    a,b = 1, 1
    length = 0
    count = 2
    while length < n:
        count += 1
        c = a + b
        a, b = b, c
        length = len(str(c))
    return count

print(fibbonacciLengthIndex(1000))
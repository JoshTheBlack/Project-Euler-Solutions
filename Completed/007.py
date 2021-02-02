# coding=utf-8
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
n = 1
while c < 10001:
    x = is_prime(n)
    n += 1
    c += x

n -= 1
t1 = time.time() 
print(f"{n} is prime number {c}")
print("Time required :", t1 - t0) 
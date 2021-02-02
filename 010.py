# coding=utf-8
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
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
n = 0
while n < 2000000:
    n += 1
    x = is_prime(n)
    if x == 1:
        c += n

t1 = time.time() 
print(f"{c} is the sum of all primes < 2 million")
print("Time required :", t1 - t0) 
# coding=utf-8
from time import perf_counter
from functools import wraps, reduce
import math

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__}: {end-start:.6f} seconds")
        return result
    return wrapper

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumDigits(n):
    n = str(n)
    x = 0
    for number in n:
        x += int(number)
    return x

def sumProperDivisors(num):
    s = set([1])
    for r in range(2, int(num**0.5)+1):
        if num % r == 0:
            s.add(r)
            s.add(num//r)
    return sum(s)

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def orderedFactors(n):
    return [[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0]
        
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

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
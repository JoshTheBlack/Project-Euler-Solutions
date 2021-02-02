# coding=utf-8
from time import perf_counter
from functools import wraps

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
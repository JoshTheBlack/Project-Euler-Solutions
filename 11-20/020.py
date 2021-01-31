# coding=utf-8
# Find the sum of the digits in the number 100!
from time import perf_counter
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__}: completed in {end-start:.6f} seconds")
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

@timed
def driver(n):
    x = factorial(n)
    y = sumDigits(x)
    return y

print(driver(100))
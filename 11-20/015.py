# coding=utf-8
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
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
@timed
def count_paths(n):
    x = factorial(n)
    return factorial(n*2)//x**2

print(count_paths(20))
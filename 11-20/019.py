# coding=utf-8
# How many Sundays fell on the first of the month in the 20th century.
from time import perf_counter
from functools import wraps
from datetime import date

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__}: completed in {end-start:.6f} seconds")
        return result
    return wrapper

@timed
def newTest(year):
    sundayFirsts = 0
    for y in range(year,year+100):
        for m in range(1,13):
            if date(y,m,1).weekday() == 6:
                sundayFirsts += 1
    return sundayFirsts

print(newTest(1901))


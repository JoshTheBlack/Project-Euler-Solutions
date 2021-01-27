# coding=utf-8
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 21000?
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

@timed
def sum_powers(num,exp):
    x = num**exp
    chars = []
    for i in range(len(str(x))):
        chars.append(int(str(x)[i]))
    return sum(chars)


print(sum_powers(2,1000))
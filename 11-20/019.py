# coding=utf-8
# How many Sundays fell on the first of the month in the 20th century.
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

def isFirstSunday(d,c):
    if d == 1 and c % 7 == 0:
        return 1
    else:
        return 0

@timed
def howMany(Year,Month,Date,dow):
    count = 0
    d31 = [1,3,5,7,8,10,12]
    d30 = [4,6,9,11]
    for y in range(Year,Year+100):
        for m in range(Month,Month+12):
            if m in d31:
                for d in range(Date,Date+31):
                    dow += 1
                    count += isFirstSunday(d,dow)
            elif m in d30:
                for d in range(Date,Date+30):
                    dow += 1
                    count += isFirstSunday(d,dow)
            elif y % 4 == 0 and y % 100 != 0:
                for d in range(Date,Date+29):
                    dow += 1
                    count += isFirstSunday(d,dow)
            elif y % 400 == 0:
                for d in range(Date,Date+29):
                    dow += 1
                    count += isFirstSunday(d,dow)
            else:
                for d in range(Date,Date+28):
                    dow += 1
                    count += isFirstSunday(d,dow)
    return count

print(howMany(1901,1,1,2))


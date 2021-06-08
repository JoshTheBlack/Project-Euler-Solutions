# coding=utf-8
# How many Sundays fell on the first of the month in the 20th century.
from datetime import date
from comm import timed

@timed
def newTest(year):
    sundayFirsts = 0
    for y in range(year,year+100):
        for m in range(1,13):
            if date(y,m,1).weekday() == 6:
                sundayFirsts += 1
    return sundayFirsts

if __name__ == "__main__":
    print(newTest(1901))


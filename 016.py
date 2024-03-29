# coding=utf-8
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
from comm import timed

@timed
def sum_powers(num,exp):
    x = 0
    for i in str(num**exp):
        x += int(i)
    return x

if __name__ == "__main__":
    print(sum_powers(2,1000))
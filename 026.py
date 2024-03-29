# coding=utf-8
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from comm import timed

def unitFraction(d, n = 1):
    res = ""
    mp = {}
    rem = n % d
    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res)
        rem *= 10
        res_part = rem // d
        res += str(res_part)
        rem = rem % d
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]

@timed
def driver():
    mp = {}
    for i in range(1, 1000):
        res = unitFraction(i)
        length = len(str(res))
        mp[length] = i
    return mp[max(mp)]

if __name__ == "__main__":
    print(driver())
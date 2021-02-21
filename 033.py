# coding=utf-8
from fractions import Fraction
from comm import timed

def findUnusualFractions():
    results = []
    count = 0

    for num in range(10,100):
        if str(num)[1] != '0':
            for den in range(num+1,100):
                numset = list(set((int(letter) for letter in str(num))))
                denset = list(set((int(letter) for letter in str(den))))
                for number in denset:
                    if number in numset:
                        numset.remove(number)
                        denset.remove(number)
                        try:
                            if numset[0] / denset[0] == num / den:
                                results.append(Fraction(num, den))
                                count += 1
                        except:
                            pass
    return results

@timed
def driver():
    results = findUnusualFractions()
    y = results[0]
    for x in range(1,len(results)):
        y *= results[x]
    return y


print(driver())
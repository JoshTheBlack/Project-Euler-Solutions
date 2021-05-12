# coding=utf-8
from comm import *

def rprime(n):
    result = n
    p = 2
    while p * p<= n :
        if n % p == 0 :
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n)))
    return int(result)

@timed
def p69(max=10):
    result = 0
    highestnpn = 0
    for n in range(2,max):
        pn = rprime(n)
        npn = n/pn
        if npn > highestnpn:
            highestnpn = npn
            result = n
    return result

def totient_function(prime_factors):
    multiplication = 1
    for factor in set(prime_factors):
        multiplication *= (1.0 - 1.0/factor)
    return 1.0/multiplication

def prime_factors_generator(n):
    prime_factors = [[i] for i in range(n+1)]
    composite = [False]*(n+1)
    for i in range(3, int(n**0.5)+1, 2):
        if not composite[i]:
            for j in range(i, n//i+1, 2):
                mul = i*j
                prime_factors[mul] = [i] + prime_factors[j]
                composite[mul] = True
    for j in range(2, n//2+1):
        mul = 2*j
        prime_factors[mul] = [2] + prime_factors[j]
        composite[mul] = True
    return prime_factors

@timed
def driver():
    pf = prime_factors_generator(1000000)
    pfnums = list(map(totient_function, pf[2:]))
    print(pfnums.index(max(pfnums))+2)

if __name__ == "__main__":
    driver()
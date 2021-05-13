# coding=utf-8
from comm import *

def totient_function(n, prime_factors):
    for factor in set(prime_factors):
        n *= (1.0 - 1.0/factor)
    return int(n)

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
    pf = prime_factors_generator(10**7)
    pfnums = list(map(totient_function, range(2,10**7), pf[2:]))
    min = 10**7
    for n in range(len(pfnums)):
        test = str(pfnums[n])
        against = str(n+2)
        if sorted(against) != sorted(test): continue
        if is_prime(n+2): continue
        if (n+2)/pfnums[n] < min: 
            min = (n+2)/pfnums[n]
            result= n+2
    return result

if __name__ == "__main__":
    print(driver())


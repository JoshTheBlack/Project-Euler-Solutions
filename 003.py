#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
from functools import reduce

def find_factors(n):    
    return sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def is_prime(z):
    n = 2
    if z < n:
        return False
    else:    
        while n < z:
            if z % n == 0:
                return False
                break
            n = n + 1
        else:
            return True

x = 600851475143

factors = find_factors(x)
primefactors = []

for i in factors:
    prime = is_prime(i)
    if prime == True:
        primefactors.append(i)
        
print(max(primefactors))
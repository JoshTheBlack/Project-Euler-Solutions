#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
from comm import is_prime, timed, factors

@timed
def largestPrimeFactor(x = 600851475143):
    facts = factors(x)
    primefactors = []
    for i in facts:
        if is_prime(i):
            primefactors.append(i)            
    return max(primefactors)

if __name__ == "__main__":
    print(largestPrimeFactor())
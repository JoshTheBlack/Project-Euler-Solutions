# coding=utf-8
# What is the smallest odd composite number that cannot be written as the sum of a prime
# and twice a square?
from comm import timed
import comm

def oddComposites():
    count = 7
    while True:
        count += 2
        if comm.is_prime(count): continue
        yield count

@timed
def p46(max = 1000):
    primes = comm.primeSieveRange(max)
    dsquares = [n for n in range(1, max) if (n/2)**0.5 % 1 == 0]
    oc = oddComposites()
    while True:
        x = next(oc)
        if x > max: break
        for ds in dsquares:
            stop = False
            if x - ds in primes: 
                stop = True
                break
        if stop == True: continue
        print(x)
        break

p46(10000)

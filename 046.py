# coding=utf-8
# What is the smallest odd composite number that cannot be written as the sum of a prime
# and twice a square?
from comm import timed
import comm

def oddCompositeGen(max=10000):
    count = 7
    while count <= max:
        count += 2
        if comm.is_prime(count): continue
        yield count

def dsquareGen(max=10000):
    x = 1
    while x <= max:
        y = 2*x**2
        if y > max: return 1
        yield y
        x += 1

# With double squares precalculated up to max
@timed
def p46(max = 1000):
    dsquares = [n for n in range(1, max) if (n/2)**0.5 % 1 == 0]
    oc = oddCompositeGen(max)
    while True:
        x = next(oc)
        if x > max: break
        stop = False
        for ds in dsquares:
            if comm.is_prime(x - ds):
                stop = True
                break
        if stop == True: continue
        print(x)
        break

# With double square generator function
@timed
def p46_2(max = 1000):
    oc = oddCompositeGen(max)
    while True:
        x = next(oc)
        if x > max: break
        dsquares = dsquareGen(x)
        stop = False
        for ds in dsquares:
            if comm.is_prime(x - ds):
                stop = True
                break
        if stop == True: continue
        return x
        break

p46(1000000)
print(p46_2(1000000))
# The actual solution to this problem is small enough that the performance difference in the two above functions are not seen until you increase
# the max value significantly.  With a large max value, p46() runs MUCH slower than p46_2().  p46_2() runs at roughly the same speed no matter the 
# max value.
from comm import timed

def cf(n):
    m = 0  #
    d = 1  #
    a0 = int(n ** 0.5) #
    an = a0
    count = 0
    if a0 != n ** 0.5:
        while an != 2*a0:
            m = d * an - m
            d = (n - m**2)/d
            an = int((a0 + m)/d)
            count += 1
    return count

@timed
def p64(max=10000):
    count = 0
    for i in range(max+1):
        if cf(i) % 2 != 0: count += 1
    return count

if __name__ == '__main__':
    print(p64())
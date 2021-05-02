# coding=utf-8
#Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, 
# and octagonal, is represented by a different number in the set.
from comm import *

def calcTri(n):
    return n*(n+1)//2

def calcSquare(n):
    return n**2

def calcPent(n):
    return n*(3*n-1)//2

def calcHex(n):
    return n*(2*n-1)

def calcHept(n):
    return n*(5*n-3)//2

def calcOct(n):
    return n*(3*n-2)

def isSquare(n):
    y = n**0.5
    if y - int(y) == 0: return True, int(y)
    return False, 0

def genTri(x = 0):
    tris = []
    while True:
        x += 1
        y = calcTri(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        tris.append(y)
    return tris

def genSquare(x = 0):
    squares = []
    while True:
        x += 1
        y = calcSquare(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        squares.append(y)
    return squares

def genPent(x = 0):
    pents = []
    while True:
        x += 1
        y = calcPent(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        pents.append(y)
    return pents

def genHex(x=0):
    hexs = []
    while True:
        x += 1
        y = calcHex(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        hexs.append(y)
    return hexs

def genHept(x=0):
    hept = []
    while True:
        x += 1
        y = calcHept(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        hept.append(y)
    return hept

def genOct(x=0):
    oct = []
    while True:
        x += 1
        y = calcOct(x)
        if len(str(y)) < 4: continue
        if len(str(y)) > 4: break
        oct.append(y)
    return oct

def findCyclical(num, l, builder=[]):
    if len(l) == 0 and str(builder[5])[2:] == str(builder[0])[:2]:
        return builder

    else:
        for row in l:
            for n in row:
                if str(num)[2:] != str(n)[:2]: continue
                builder.append(n)
                if findCyclical(n, [li for li in l if li != row], builder):
                    return builder
                else: 
                    builder.remove(n)
    #builder = []
    return False

# oct 1281, hex 8128, pent 2882, tri 8256, sq 5625, hept 2512
@timed
def p61():
    tris = genTri()
    sq = genSquare()
    pents = genPent()
    hexs = genHex()
    hepts = genHept()
    octs = genOct()

    for oct in octs:
        x = findCyclical(oct,[tris,sq,pents,hexs,hepts], [oct])
        if x: return sum(x)

if __name__ == "__main__":
    print(p61())


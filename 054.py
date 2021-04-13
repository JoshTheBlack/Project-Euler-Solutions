# coding=utf-8
# !Royal Flush > !Straight Flush > !Four of a Kind > !Full house > !Flush > !Straight > !3 of kind > !two pair > !pair > !high card
from comm import *
import os
import numpy as np

@timed
def importData():
    data = np.loadtxt(os.path.join(os.sys.path[0], "p054_poker.txt"), dtype=str, skiprows=0, delimiter=" ")
    return data

def isHandFlush(hand):
    isFlush = True
    for i in range(1, len(hand)):
        if hand[i][1] != hand[i-1][1]:
            isFlush = False
            break
    return isFlush

def isHandStraight(hand):
    isStraight = True
    for i in range(1, len(hand)):
        #if hand[4][0] == 14 and hand[0][0] == 2:
        if hand[i][0] != hand[i-1][0] + 1:
            if i == 4 and hand[i][0] == 14 and hand[0][0] == 2:
                continue
            isStraight = False
            break
    return isStraight

def isHandRoyal(hand):
    for i in range(len(hand)):
        if hand[i][0] != 10+i: return False
    return True

def countPairs(hand):
    import collections
    d = collections.defaultdict(int)
    for i in range(len(hand)):
        d[hand[i][0]] += 1
    if len(d) == 5: return 0, hand[4][0]
    if len(d) == 4: 
        for i in sorted(d, key=d.get):
            if d[i] == 2: return 1, i
    if len(d) == 3: 
        hc = 0
        for i in sorted(d, key=d.get):
            if i > hc and d[i] == 2: hc = i
            if d[i] == 3: return "3K", i
        return 2, hc
    if len(d) == 2:
        for i in sorted(d, key=d.get):
            if d[i] == 3: return "FH", i
        return "4K", hand[2][0]
    
def buildHands(hands):
    newhand = []
    newhand2 = []
    for i in range(5):
        newhand.append([hands[i][0:-1],hands[i][-1:]])
        if newhand[i][0] == "T": newhand[i][0] = 10
        if newhand[i][0] == "J": newhand[i][0] = 11
        if newhand[i][0] == "Q": newhand[i][0] = 12
        if newhand[i][0] == "K": newhand[i][0] = 13
        if newhand[i][0] == "A": newhand[i][0] = 14
        newhand[i][0] = int(newhand[i][0])
    for i in range(5,10):
        newhand2.append([hands[i][0:-1],hands[i][-1:]])
        if newhand2[i-5][0] == "T": newhand2[i-5][0] = 10
        if newhand2[i-5][0] == "J": newhand2[i-5][0] = 11
        if newhand2[i-5][0] == "Q": newhand2[i-5][0] = 12
        if newhand2[i-5][0] == "K": newhand2[i-5][0] = 13
        if newhand2[i-5][0] == "A": newhand2[i-5][0] = 14
        newhand2[i-5][0] = int(newhand2[i-5][0])
    return sorted(newhand), sorted(newhand2)
    
def scoreHand(hand):
    flush = isHandFlush(hand)
    straight = isHandStraight(hand)
    royal = isHandRoyal(hand)
    pairs, hc = countPairs(hand)
    if royal and flush: return 180
    if straight and flush: return 160+hc
    if pairs == "4K": return 140+hc
    if pairs == "FH": return 120+hc
    if pairs == 0 and flush: return 100+hc
    if pairs == 0 and straight: return 80 + hc
    if pairs == "3K": return 60+hc
    if pairs == 2: return 40+hc
    if pairs == 1: return 20+hc
    return hc
    
@timed
def p54():
    result = 0
    for i in data:
        x,y = buildHands(i)
        if scoreHand(x) > scoreHand(y):
            result += 1
    return result

if __name__ == "__main__":
    data = importData()
    print(p54())
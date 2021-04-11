# coding=utf-8
# Royal Flush > Straight Flush > Four of a Kind > Full house > Flush > Straight > 3 of kind > two pair > pair > high card
from comm import *
import os
import numpy as np

data = np.loadtxt(os.path.join(os.sys.path[0], "p054_poker.txt"), dtype=str, skiprows=0, delimiter=" ")

def isHandFlush(hand):
    isFlush = True
    for i in range(1, len(hand)):
        if hand[i][1] != hand[i-1][1]:
            isFlush = False
            break
    return isFlush

def isHandStraight(hand):
    hand = sorted(hand)
    #for i in range(1, len(hand)):
    print(hand)
    

def buildHands(hands):
    newhand = []
    newhand2 = []
    for i in range(5):
        newhand.append([hands[i][0:1],hands[i][1:2]])
        if newhand[i][0] == "j": newhand[i][0] = 11
        if newhand[i][0] == "q": newhand[i][0] = 12
        if newhand[i][0] == "k": newhand[i][0] = 13
        if newhand[i][0] == "a": newhand[i][0] = 14
    for i in range(5,10):
        newhand2.append([hands[i][0:1],hands[i][1:2]])
        if newhand2[i][0] == "j": newhand2[i-5][0] = 11
        if newhand2[i][0] == "q": newhand2[i-5][0] = 12
        if newhand2[i][0] == "k": newhand2[i-5][0] = 13
        if newhand2[i][0] == "a": newhand2[i-5][0] = 14
    return newhand, newhand2
    

    print(isFlush)
 
x,y = buildHands(["ah", "5h", "4h", "2h", "6h", "5d","4d","qh","as","kc"])
print(x,y)
# def didP1Win(p1hand,p2hand):

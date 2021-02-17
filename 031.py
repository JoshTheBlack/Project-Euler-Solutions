# coding=UTF-8
from comm import timed

def count(coins, total): # Array of coin denominatons, total you want to calculate routes to.
    table = [0 for i in range(total+1)] 
    table[0] = 1
    for i in range(0,len(coins)): 
        for j in range(coins[i],total+1): 
            table[j] += table[j-coins[i]] 
  
    return table[total]

@timed
def driver():
    array = [1,2,5,10,20,50,100,200]
    total = 200
    print(count(array,total))

driver()
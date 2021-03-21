# coding=utf-8
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
# how many are triangle words?
import numpy as np
from comm import timed
import os
from collections import Counter

# Pull words in from file and store in a list called words.
words = np.transpose(np.loadtxt(os.path.join(os.sys.path[0], "p042_words.txt"), dtype=str, skiprows=0, delimiter=','))
words = np.char.strip(words, '"')

def calcWordValue(word):
    value = 0
    for letter in word.lower():
        value += ord(letter) - 96
    return value

@timed
def p42(words):
    # Calculate the numerical value of words and store it in a list called wordValues
    wordValues = []
    for word in words:
        wordValues.append(calcWordValue(word))
    # Find the max value in wordValues and store it as max
    maxi = max(wordValues)
    stop,count,triangles = 0, 1, []
    # Loop through triangle number values 1-max, storing in a list called triangles
    while maxi >= stop:
        stop = int(0.5*count*(count+1))
        triangles.append(stop)
        count += 1
    # count instances of each value in wordValues and store as a dictionary called wordValueDict
    wordValueDict = Counter(wordValues)
    count = 0 #reset counter
    # loop through triangle numbers.  If they exist in the wordValueDict, add their number of occurrences to count.
    for triangle in triangles:
        count += wordValueDict[triangle]
    return count

print(p42(words))
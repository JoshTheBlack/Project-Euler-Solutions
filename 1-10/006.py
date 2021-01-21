# coding=utf-8
# The sum of the squares of the first ten natural numbers is 385 (1sq + 2sq ... +10sq)
#
# The square of the sum of the first ten natural numbers is 3025 (1+2+3..+10)squared = 55sq = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
squareofsums = 0
sumofsquares = 0
numberRange = 100

for num in range(1,numberRange + 1):
    squareofsums += num

squareofsums *= squareofsums

for num in range(1,numberRange +1):
    sumofsquares += num * num

answer = squareofsums - sumofsquares
print(answer)
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

x = 1000
y=0
z=0
numbers3 = []
output = 0

while y<x:
    numbers3.append(y)
    y=y+3

while z<x:
    if z % 3 != 0:
        numbers3.append(z)
        z=z+5
    else:
        z=z+5

for numbers in numbers3:
    output = output + numbers

print(output)
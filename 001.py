#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
from comm import timed

@timed
def driver(max=1000, *args):
    '''Function to add up all multiples of *args less than max.'''
    args = list(args)
    result = 0
    for x in range(max+1):
        if any(x % y == 0 for y in args):
            result += x
    return result


if __name__ == "__main__":
    print(driver(1000, 3, 5))
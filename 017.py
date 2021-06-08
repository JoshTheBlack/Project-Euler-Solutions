# coding=utf-8
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
# # 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
from comm import timed

class Solution(object):
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
        "Nineteen"]
    tens = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
        "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        ans = ""
        i = 0
        while num > 0:
            if num % 1000 != 0 and num % 100 != 0:
                ans = self.helper(num % 10000) + Solution.thousands[i] + " " + ans
                i += 1
                num //= 1000
            elif num % 1000 == 0:
                ans = self.helper(num // 1000) + "Thousand"
            elif num % 100 == 0:
                ans = self.helper(num // 100) + "Hundred"
            return ans.strip()

    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return Solution.less_than_20[n]
        elif n < 100:
            return Solution.tens[n//10] + self.helper(n % 10)
        elif n < 1000:
            return Solution.less_than_20[n // 100] + "Hundred" + "and" + self.helper(n % 100)
        else:
            return Solution.less_than_20[n // 1000] + "Thousandand" + self.helper(n % 1000)


@timed
def count_letters(x,y):
    count = 0
    for i in range(x,y+1):
        count += len(ob.numberToWords(i))
    return count

if __name__ == "__main__":
    ob = Solution()
    print(count_letters(1,1000))
# coding=utf-8
# 29. Divide Two Integers
# Difficulty: Medium
#
# >Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.



#My recursive solution
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient, remainder = self.divide_helper(dividend, divisor)
        if not positive:
            quotient = -quotient
            remainder = -remainder
        return min(2147483647, max(quotient, -2147483648)) #restrict the range

    def divide_helper(self, dividend, divisor):
        if dividend == 0:
            return 0, 0
        else:
            quotient, remainder = self.divide_helper(dividend >> 1, divisor) #recursive

        quotient <<= 1
        remainder <<= 1

        if (dividend & 1) == 1: #dividend is odd
            remainder += 1

        if remainder >= divisor: #!!!! is >=   not >
            remainder -= divisor
            quotient += 1
        return quotient, remainder


#https://leetcode.com/discuss/25029/clear-python-code
class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        #当dividend >= divisor时，那么我们可以减去k * divisor，其中k = sum(2^0, 2^1,...)
        while dividend >= divisor:
            temp, i = divisor, 1
            #在每一轮中减去(2^i) * divisor，逐步减小dividend的值,并且将(2^i)记录在res中
            while dividend >= temp:
#                 dividend -= temp
#                 res += i
#                i <<= 1
#                temp <<= 1
                dividend, res =  dividend - temp, res + i
                i, temp = i << 1, temp << 1
#                dividend, res, i, temp =  dividend - temp, res + i, i << 1, temp << 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

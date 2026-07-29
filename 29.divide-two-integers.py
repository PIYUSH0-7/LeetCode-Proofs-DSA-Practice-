#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        is_negative = (dividend < 0) != (divisor < 0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            current_quotient_bit = 1
            
            while (temp_divisor << 1) <= abs_dividend:
                temp_divisor <<= 1
                current_quotient_bit <<= 1
            
            abs_dividend -= temp_divisor
            quotient += current_quotient_bit
        
        if is_negative:
            quotient = -quotient
        
        return max(MIN_INT, min(MAX_INT, quotient))
# @lc code=end

#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10

            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and digit > 7):
                return 0
            if reversed_x < -(2**31) // 10 or (reversed_x == -(2**31) // 10 and digit > 8):
                return 0
                
            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x
# @lc code=end

#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calculate_positive_power(base: float, exponent: int) -> float:
            result = 1.0
            current_base = base
            current_exponent = exponent

            while current_exponent > 0:
                if current_exponent % 2 == 1:
                    result *= current_base
                current_base *= current_base
                current_exponent //= 2
            return result

        if n < 0:
            return 1.0 / calculate_positive_power(x, -n)
        else:
            return calculate_positive_power(x, n)
# @lc code=end

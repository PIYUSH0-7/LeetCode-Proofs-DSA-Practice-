#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # 1162261467 is 3^19, the largest power of 3 that fits within a signed 32-bit integer.
        # If n is a power of three, it must be of the form 3^x.
        # For n to be a valid input and a power of three, x must be between 0 and 19 (inclusive).
        # Any 3^x for 0 <= x <= 19 will be a divisor of 3^19.
        # Any other positive integer n that is not a power of three will not divide 3^19.
        return 1162261467 % n == 0
# @lc code=end

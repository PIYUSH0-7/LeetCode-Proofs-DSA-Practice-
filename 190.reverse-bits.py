#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for _ in range(32):
            reversed_num <<= 1
            reversed_num |= (n & 1)
            n >>= 1
        return reversed_num
# @lc code=end

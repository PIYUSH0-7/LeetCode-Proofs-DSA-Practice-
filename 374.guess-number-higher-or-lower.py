#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else: # result == 1
                low = mid + 1
        
        return -1 # Should not be reached based on problem constraints and guarantee
# @lc code=end

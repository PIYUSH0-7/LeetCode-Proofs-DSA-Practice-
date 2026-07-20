#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else: # square > num
                right = mid - 1
        
        return False
# @lc code=end

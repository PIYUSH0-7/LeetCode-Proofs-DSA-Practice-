#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
# @lc code=end

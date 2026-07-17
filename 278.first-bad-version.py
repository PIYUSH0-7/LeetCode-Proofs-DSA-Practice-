#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        first_bad = n 

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return first_bad
# @lc code=end

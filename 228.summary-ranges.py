#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        n = len(nums)
        i = 0
        while i < n:
            start_val = nums[i]
            j = i
            while j + 1 < n and nums[j+1] == nums[j] + 1:
                j += 1
            
            end_val = nums[j]
            
            if start_val == end_val:
                ranges.append(str(start_val))
            else:
                ranges.append(f"{start_val}->{end_val}")
            
            i = j + 1
            
        return ranges
# @lc code=end

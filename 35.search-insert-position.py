#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # This will store the potential insertion index.
        # Initialize to len(nums) for the case where target is greater than all elements.
        insertion_index = len(nums) 

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else: # nums[mid] > target
                # This mid could be the insertion point (or smaller)
                insertion_index = mid
                right = mid - 1
        
        return insertion_index
# @lc code=end

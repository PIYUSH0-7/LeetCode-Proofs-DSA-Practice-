#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_idx = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[write_idx - 1]:
                nums[write_idx] = nums[i]
                write_idx += 1
                
        return write_idx
# @lc code=end

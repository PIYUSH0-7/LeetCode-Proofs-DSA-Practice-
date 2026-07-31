#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far
# @lc code=end

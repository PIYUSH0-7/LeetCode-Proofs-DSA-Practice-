#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal_index = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i
        
        return goal_index == 0
# @lc code=end

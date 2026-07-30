#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_reach = 0
        max_reach_next_jump = 0

        for i in range(n - 1):
            max_reach_next_jump = max(max_reach_next_jump, i + nums[i])

            if i == current_reach:
                jumps += 1
                current_reach = max_reach_next_jump
                if current_reach >= n - 1:
                    break
        
        return jumps
# @lc code=end

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # ways_one_step_ago represents dp[i-1]
        # ways_two_steps_ago represents dp[i-2]
        ways_two_steps_ago = 1 
        ways_one_step_ago = 2 
        
        for _ in range(3, n + 1):
            current_ways = ways_one_step_ago + ways_two_steps_ago
            ways_two_steps_ago = ways_one_step_ago
            ways_one_step_ago = current_ways
            
        return ways_one_step_ago
# @lc code=end

#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Calculate the total number of steps required to reach the destination.
        # To go from (0,0) to (m-1, n-1), we need m-1 down moves and n-1 right moves.
        # Total steps = (m-1) + (n-1) = m + n - 2.
        total_steps = m + n - 2
        
        # We need to choose either (m-1) down moves out of total_steps,
        # or (n-1) right moves out of total_steps.
        # Both are equivalent to C(total_steps, m-1) or C(total_steps, n-1).
        # For efficiency, we choose the smaller of the two for K in C(N, K).
        # K = min(m-1, n-1)
        k = min(m - 1, n - 1)

        # C(N, K) = N * (N-1) * ... * (N-K+1) / (K * (K-1) * ... * 1)
        res = 1
        for i in range(k):
            res = res * (total_steps - i) // (i + 1)
            
        return res
# @lc code=end

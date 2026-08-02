#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initialize first row sums
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        # Initialize first column sums
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        # Fill the rest of the grid with minimum path sums
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]
# @lc code=end

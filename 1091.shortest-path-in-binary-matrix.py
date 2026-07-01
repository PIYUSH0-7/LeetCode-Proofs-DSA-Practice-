#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # Directions: 8 possible moves
        directions = [(1,0), (-1,0), (0,1), (0,-1),
                      (1,1), (1,-1), (-1,1), (-1,-1)]
        
        # BFS queue: (row, col, path_length)
        queue = deque([(0,0,1)])
        visited = set((0,0))
        
        while queue:
            r, c, length = queue.popleft()
            
            # Destination reached
            if (r, c) == (n-1, n-1):
                return length
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,length+1))
        
        return -1

# @lc code=end


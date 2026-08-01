#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        num = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # Move right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # Move down
            if top > bottom:
                break
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # Move left
            if left > right:
                break
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # Move up
            if top > bottom:
                break
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix
# @lc code=end

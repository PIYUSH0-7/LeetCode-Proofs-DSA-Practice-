#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            row = mid // n
            col = mid % n
            
            current_val = matrix[row][col]
            
            if current_val == target:
                return True
            elif current_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
# @lc code=end

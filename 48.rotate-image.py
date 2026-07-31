#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row
        for r in range(n):
            matrix[r].reverse()
# @lc code=end

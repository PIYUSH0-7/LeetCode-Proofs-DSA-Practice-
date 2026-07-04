#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        if numRows == 0:
            return triangle

        triangle.append([1])

        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            current_row = [1]

            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])
            
            current_row.append(1)
            triangle.append(current_row)
            
        return triangle
# @lc code=end

#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        row = [1]

        for k in range(1, rowIndex + 1):
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)
            
        return row
# @lc code=end

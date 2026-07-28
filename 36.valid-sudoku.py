#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue

                if char in rows[r]:
                    return False
                rows[r].add(char)

                if char in cols[c]:
                    return False
                cols[c].add(char)

                box_idx = (r // 3) * 3 + (c // 3)
                if char in boxes[box_idx]:
                    return False
                boxes[box_idx].add(char)
        
        return True
# @lc code=end

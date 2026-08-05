#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        current_combo = []

        def backtrack(start_num):
            if len(current_combo) == k:
                combinations.append(list(current_combo))
                return

            remaining_needed = k - len(current_combo)
            upper_bound = n - remaining_needed + 1

            for num in range(start_num, upper_bound + 1):
                current_combo.append(num)
                backtrack(num + 1)
                current_combo.pop()

        backtrack(1)
        return combinations
# @lc code=end

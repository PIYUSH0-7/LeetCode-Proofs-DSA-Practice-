#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(current_string, open_count, close_count):
            if len(current_string) == 2 * n:
                ans.append(current_string)
                return

            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans
# @lc code=end

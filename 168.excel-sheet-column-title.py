#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            columnNumber //= 26
        return "".join(result[::-1])
# @lc code=end

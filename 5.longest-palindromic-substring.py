#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

        for i in range(n):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)

        return s[start : start + max_len]
# @lc code=end

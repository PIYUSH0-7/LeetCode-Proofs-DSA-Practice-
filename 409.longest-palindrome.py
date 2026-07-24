#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = collections.Counter(s)
        
        total_length = 0
        found_odd_count = False
        
        for count in char_counts.values():
            total_length += (count // 2) * 2
            if count % 2 == 1:
                found_odd_count = True
                
        if found_odd_count:
            total_length += 1
            
        return total_length
# @lc code=end

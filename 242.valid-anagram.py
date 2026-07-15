#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = [0] * 26

        for char_s in s:
            char_counts[ord(char_s) - ord('a')] += 1
        
        for char_t in t:
            char_counts[ord(char_t) - ord('a')] -= 1
        
        for count in char_counts:
            if count != 0:
                return False
        
        return True
# @lc code=end

#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = collections.Counter(magazine)
        
        for char in ransomNote:
            if magazine_counts[char] > 0:
                magazine_counts[char] -= 1
            else:
                return False
                
        return True
# @lc code=end

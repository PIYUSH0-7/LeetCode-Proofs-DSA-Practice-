#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            
            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []
            
            anagram_groups[sorted_s].append(s)
            
        return list(anagram_groups.values())
# @lc code=end

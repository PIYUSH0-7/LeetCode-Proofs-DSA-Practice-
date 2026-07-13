#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_to_t_map = {}
        t_to_s_map = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t_map:
                if s_to_t_map[char_s] != char_t:
                    return False
            else:
                s_to_t_map[char_s] = char_t
            
            if char_t in t_to_s_map:
                if t_to_s_map[char_t] != char_s:
                    return False
            else:
                t_to_s_map[char_t] = char_s
                
        return True
# @lc code=end

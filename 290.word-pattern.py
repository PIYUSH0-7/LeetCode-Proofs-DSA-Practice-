#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False
            
        char_to_word_map = {}
        word_to_char_map = {}
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            if char in char_to_word_map:
                if char_to_word_map[char] != word:
                    return False
            else:
                char_to_word_map[char] = word
            
            if word in word_to_char_map:
                if word_to_char_map[word] != char:
                    return False
            else:
                word_to_char_map[word] = char
                
        return True
# @lc code=end

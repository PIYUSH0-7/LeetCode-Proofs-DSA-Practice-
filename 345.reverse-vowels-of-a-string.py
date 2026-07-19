#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        left = 0
        right = len(chars) - 1
        
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            
            while left < right and chars[right] not in vowels:
                right -= 1
            
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return "".join(chars)
# @lc code=end

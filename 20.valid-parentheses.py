#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:  # It's a closing bracket
                if not stack:
                    return False
                
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack
# @lc code=end

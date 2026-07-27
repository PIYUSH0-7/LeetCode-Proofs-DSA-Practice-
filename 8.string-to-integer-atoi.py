#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        sign = 1 
        
        # 2. Determine signedness
        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
                
        value = 0
        
        # 3. Conversion
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for potential overflow
            if sign == 1:
                if value > INT_MAX // 10 or (value == INT_MAX // 10 and digit > INT_MAX % 10):
                    return INT_MAX
            else: # sign == -1
                # abs(INT_MIN) is 2**31, which is INT_MAX + 1
                if value > (INT_MAX + 1) // 10 or (value == (INT_MAX + 1) // 10 and digit > (INT_MAX + 1) % 10):
                    return INT_MIN
            
            value = value * 10 + digit
            i += 1
            
        # 4. Rounding (clamping) is handled during conversion
        return value * sign
# @lc code=end

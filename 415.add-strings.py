#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0

        while p1 >= 0 or p2 >= 0 or carry:
            digit1 = int(num1[p1]) if p1 >= 0 else 0
            digit2 = int(num2[p2]) if p2 >= 0 else 0

            current_sum = digit1 + digit2 + carry
            carry = current_sum // 10
            current_digit = current_sum % 10
            
            res.append(str(current_digit))
            
            p1 -= 1
            p2 -= 1
        
        return "".join(res[::-1])
# @lc code=end

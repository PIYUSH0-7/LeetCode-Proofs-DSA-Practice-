#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If we reach here, it means all digits were 9 (e.g., [9], [9,9])
        # We need to prepend a 1 to the array.
        return [1] + digits
# @lc code=end

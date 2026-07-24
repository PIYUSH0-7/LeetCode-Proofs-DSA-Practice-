#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_map = "0123456789abcdef"
        hex_digits = []

        # For negative numbers, Python's default behavior for bitwise operations
        # like `&` on negative numbers will automatically provide the two's complement
        # representation within the specified bit width.
        # We simulate a 32-bit unsigned integer by using the mask 0xFFFFFFFF.
        # This converts negative numbers to their 32-bit unsigned equivalent
        # (e.g., -1 becomes 4294967295) and leaves positive numbers unchanged
        # within the 32-bit range.
        unsigned_num = num & 0xFFFFFFFF 

        while unsigned_num > 0:
            remainder = unsigned_num % 16
            hex_digits.append(hex_map[remainder])
            unsigned_num //= 16
        
        # The digits are collected in reverse order (least significant first).
        # We need to reverse the list and then join them to form the final string.
        return "".join(hex_digits[::-1])
# @lc code=end

#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = []
        num_digits = len(digits)

        def backtrack(index, current_combination):
            if index == num_digits:
                result.append(current_combination)
                return

            digit = digits[index]
            letters = phone_map[digit]
            for char_val in letters:
                backtrack(index + 1, current_combination + char_val)

        backtrack(0, "")
        return result
# @lc code=end

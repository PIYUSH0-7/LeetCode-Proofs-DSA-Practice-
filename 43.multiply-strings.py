#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)
        
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(n2 - 1, -1, -1):
                digit2 = int(num2[j])

                prod = digit1 * digit2

                # Positions where the product contributes:
                # i + j + 1 is for the unit's place of the product (e.g., 8 in 18)
                # i + j is for the ten's place (carry) of the product (e.g., 1 in 18)
                pos_unit = i + j + 1
                pos_carry = i + j

                current_sum = result[pos_unit] + prod
                
                result[pos_unit] = current_sum % 10
                result[pos_carry] += current_sum // 10
        
        start_index = 0
        while start_index < len(result) - 1 and result[start_index] == 0:
            start_index += 1
            
        return "".join(map(str, result[start_index:]))
# @lc code=end

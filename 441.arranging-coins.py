#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # We need to find the largest integer k such that the sum of coins for k rows is less than or equal to n.
        # The sum of coins for k rows is given by the formula k * (k + 1) / 2.
        # So, we are looking for the largest k such that k * (k + 1) / 2 <= n.
        # This inequality can be rearranged into a quadratic form:
        # k^2 + k <= 2n
        # k^2 + k - 2n <= 0

        # To find the roots of the quadratic equation k^2 + k - 2n = 0, we use the quadratic formula:
        # k = (-b +/- sqrt(b^2 - 4ac)) / 2a
        # Here, a=1, b=1, c=-2n.
        # k = (-1 +/- sqrt(1^2 - 4 * 1 * (-2n))) / (2 * 1)
        # k = (-1 +/- sqrt(1 + 8n)) / 2

        # Since k must be a positive number of rows, we take the positive root:
        # k = (-1 + sqrt(1 + 8n)) / 2

        # The function k^2 + k - 2n is a parabola opening upwards.
        # The inequality k^2 + k - 2n <= 0 holds for k values between its two roots.
        # The largest integer k that satisfies the inequality will be the floor of the positive root.

        # Calculate the value under the square root
        discriminant = 1 + 8 * n
        
        # Calculate the positive root using math.sqrt (which returns a float)
        k_float = (-1 + math.sqrt(discriminant)) / 2
        
        # Convert the float result to an integer. For positive numbers, int() truncates towards zero,
        # which is equivalent to the floor function for this problem.
        return int(k_float)
# @lc code=end

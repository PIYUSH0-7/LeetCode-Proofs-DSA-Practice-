#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            val = abs(nums[i])
            # The number `val` means we've seen `val`.
            # Mark its corresponding index `val - 1` by making the number at that index negative.
            # We use `abs(nums[i])` to handle cases where `nums[i]` itself was already made negative.
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
        
        disappeared = []
        for i in range(n):
            # If nums[i] is still positive, it means the number `i + 1` was never encountered
            # in the original array (because if it were, nums[i] would have been made negative).
            if nums[i] > 0:
                disappeared.append(i + 1)
        
        return disappeared
# @lc code=end

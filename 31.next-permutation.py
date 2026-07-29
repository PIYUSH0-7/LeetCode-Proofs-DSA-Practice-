#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the first decreasing element from the right
        # Find index 'i' such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # If such an 'i' is found (array is not completely reverse sorted)
        if i >= 0:
            # Step 2: Find the smallest element to the right of 'i' that is greater than nums[i]
            # Find index 'j' such that nums[j] > nums[i]
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray from i + 1 to the end
        # This handles both cases:
        # 1. If 'i' was found, the suffix needs to be sorted in ascending order.
        # 2. If no 'i' was found (array was reverse sorted, i.e., i is -1), then 
        #    we reverse the entire array to get the smallest permutation.
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# @lc code=end

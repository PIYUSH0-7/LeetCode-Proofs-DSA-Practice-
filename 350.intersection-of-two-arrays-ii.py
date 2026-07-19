#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
import collections
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ensure nums1 is the smaller array to optimize space for the counter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counts = collections.Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        
        return result
# @lc code=end

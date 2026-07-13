#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index:
                prev_index = num_to_index[num]
                if abs(i - prev_index) <= k:
                    return True
            num_to_index[num] = i
        return False
# @lc code=end

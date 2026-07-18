#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0]
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_sums.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

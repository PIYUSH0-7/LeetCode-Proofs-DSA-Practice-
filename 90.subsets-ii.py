#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        current_subset = []
        nums.sort()

        def backtrack(start_index):
            results.append(list(current_subset))

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue

                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()

        backtrack(0)
        return results
# @lc code=end

#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        n = len(nums)
        visited = [False] * n

        def backtrack(current_permutation):
            if len(current_permutation) == n:
                results.append(list(current_permutation))
                return

            for i in range(n):
                if visited[i]:
                    continue

                # Skip duplicates: if the current number is the same as the previous number,
                # and the previous number has NOT been visited, skip the current number.
                # This ensures that for duplicate numbers, we only consider them in a specific order
                # (e.g., use the first '1' before the second '1' in [1,1,2]).
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                current_permutation.append(nums[i])
                visited[i] = True
                backtrack(current_permutation)
                visited[i] = False
                current_permutation.pop()

        backtrack([])
        return results
# @lc code=end

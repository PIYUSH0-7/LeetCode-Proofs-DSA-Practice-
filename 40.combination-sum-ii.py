#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            if remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remaining_target:
                    break

                current_combination.append(candidates[i])
                backtrack(current_combination, remaining_target - candidates[i], i + 1)
                current_combination.pop()

        backtrack([], target, 0)
        return results
# @lc code=end

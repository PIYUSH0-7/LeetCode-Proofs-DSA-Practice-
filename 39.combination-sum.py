#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        candidates.sort()

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                if candidate > remaining_target:
                    break
                
                current_combination.append(candidate)
                backtrack(current_combination, remaining_target - candidate, i)
                current_combination.pop()

        backtrack([], target, 0)
        return results
# @lc code=end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        def backtrack(current_permutation, used):
            if len(current_permutation) == n:
                result.append(list(current_permutation))
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    
                    backtrack(current_permutation, used)
                    
                    current_permutation.pop()
                    used[i] = False
        
        backtrack([], [False] * n)
        
        return result
# @lc code=end

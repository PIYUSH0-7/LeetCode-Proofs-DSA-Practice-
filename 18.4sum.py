#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        results = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Optimization: If the smallest possible sum starting with nums[i] is already greater than target
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            # Optimization: If the largest possible sum starting with nums[i] is less than target
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Optimization: If the smallest possible sum starting with nums[i] and nums[j] is already greater than target
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                # Optimization: If the largest possible sum starting with nums[i] and nums[j] is less than target
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue

                left = j + 1
                right = n - 1
                current_target_sum = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == current_target_sum:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        left += 1
                        right -= 1
                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif current_sum < current_target_sum:
                        left += 1
                    else: # current_sum > current_target_sum
                        right -= 1
        
        return results
# @lc code=end

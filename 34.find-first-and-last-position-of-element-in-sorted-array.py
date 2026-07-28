#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first(nums_arr, target_val):
            left, right = 0, len(nums_arr) - 1
            first_pos = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums_arr[mid] == target_val:
                    first_pos = mid
                    right = mid - 1
                elif nums_arr[mid] < target_val:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos

        def find_last(nums_arr, target_val):
            left, right = 0, len(nums_arr) - 1
            last_pos = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums_arr[mid] == target_val:
                    last_pos = mid
                    left = mid + 1
                elif nums_arr[mid] < target_val:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos
        
        if not nums:
            return [-1, -1]

        start_index = find_first(nums, target)
        if start_index == -1:
            return [-1, -1]
        
        end_index = find_last(nums, target)
        
        return [start_index, end_index]
# @lc code=end

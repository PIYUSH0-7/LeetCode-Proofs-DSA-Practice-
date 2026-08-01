#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        for current_interval in intervals:
            if not merged_intervals or current_interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(current_interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], current_interval[1])
        
        return merged_intervals
# @lc code=end

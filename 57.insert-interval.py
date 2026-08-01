#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        new_start, new_end = newInterval[0], newInterval[1]
        
        i = 0
        n = len(intervals)
        
        # Add all intervals that come before newInterval and do not overlap
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
            
        # Merge overlapping intervals
        # An overlap exists if interval.start <= new_end and interval.end >= new_start
        # Since intervals are sorted by start, and we already handled intervals[i][1] < new_start,
        # the condition for overlap simplifies to intervals[i][0] <= new_end
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
            
        # Add the merged newInterval
        result.append([new_start, new_end])
        
        # Add all intervals that come after newInterval and do not overlap
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result
# @lc code=end

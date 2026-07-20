#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible_times = []
        for h in range(12):
            for m in range(60):
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    possible_times.append(f"{h}:{m:02d}")
        return possible_times
# @lc code=end

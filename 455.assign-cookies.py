#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_ptr = 0
        cookie_ptr = 0
        content_count = 0

        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                content_count += 1
                child_ptr += 1
                cookie_ptr += 1
            else:
                # Current cookie is too small for current child, try the next cookie
                cookie_ptr += 1
        
        return content_count
# @lc code=end

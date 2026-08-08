#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # If a string 's' can be constructed by taking a substring 'p' and
        # appending multiple copies of 'p' together (i.e., s = p + p + ... + p
        # where 'p' appears k times and k >= 2), then 's' must be present
        # within the string (s + s) but with its first and last characters removed.
        #
        # Let s = "abab". Then s+s = "abababab".
        # (s+s)[1:-1] = "bababa". "abab" is a substring of "bababa".
        #
        # Let s = "abcabc". Then s+s = "abcabcabcabc".
        # (s+s)[1:-1] = "bcabcabcab". "abcabc" is a substring of "bcabcabcab".
        #
        # If s itself is the smallest repeating unit (e.g., s = "abc", k=1),
        # then (s+s)[1:-1] = "bcab". "abc" is NOT a substring of "bcab".
        # This correctly handles the "multiple copies" requirement.
        
        return s in (s + s)[1:-1]
# @lc code=end

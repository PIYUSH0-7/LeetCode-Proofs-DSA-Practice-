#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp_prev2 represents the number of ways to decode s[:i-2] (dp[i-2])
        # dp_prev1 represents the number of ways to decode s[:i-1] (dp[i-1])
        # dp_curr represents the number of ways to decode s[:i] (dp[i])

        # Base case for dp[0]: An empty string has 1 way to be decoded (do nothing).
        dp_prev2 = 1 

        # Base case for dp[1]:
        # If the first character s[0] is '0', it cannot be decoded, so 0 ways.
        # Otherwise, s[0] can be decoded as a single digit, so 1 way.
        dp_prev1 = 0 if s[0] == '0' else 1

        # Iterate from the second character up to the end of the string.
        # 'i' represents the length of the prefix being considered (s[0...i-1]).
        # The loop calculates dp[i].
        for i in range(2, n + 1):
            dp_curr = 0

            # Option 1: Decode the last character s[i-1] as a single digit.
            # This is valid only if s[i-1] is not '0'.
            # If valid, add the number of ways to decode s[:i-1] (dp_prev1).
            if s[i-1] != '0':
                dp_curr += dp_prev1

            # Option 2: Decode the last two characters s[i-2:i] as a two-digit number.
            # This is valid if:
            # 1. The first digit of the two-digit number (s[i-2]) is not '0'.
            #    (e.g., "06" is not a valid two-digit decoding).
            # 2. The integer value of the two-digit number is between 10 and 26.
            two_digit_val = int(s[i-2:i])
            if s[i-2] != '0' and 10 <= two_digit_val <= 26:
                # If valid, add the number of ways to decode s[:i-2] (dp_prev2).
                dp_curr += dp_prev2
            
            # Update dp_prev2 and dp_prev1 for the next iteration.
            # dp_prev2 becomes the old dp_prev1.
            # dp_prev1 becomes the newly calculated dp_curr.
            dp_prev2 = dp_prev1
            dp_prev1 = dp_curr
        
        # After the loop, dp_prev1 holds the total number of ways to decode the entire string s (dp[n]).
        return dp_prev1
# @lc code=end

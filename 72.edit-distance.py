#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Optimize space by ensuring word2 is the shorter string,
        # so our DP array (rows) has the smaller dimension.
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m

        # dp[j] will store the minimum operations to convert word1[:i] to word2[:j]
        # for the current row i.
        # prev_row[j] stores dp[i-1][j].
        # Initialize prev_row for the base case i=0 (converting empty string to word2[:j]).
        # This means transforming "" to word2[:j] takes j insertions.
        prev_row = list(range(n + 1))

        for i in range(1, m + 1):
            curr_row = [0] * (n + 1)
            # Base case for current row i: converting word1[:i] to an empty string.
            # This means transforming word1[:i] to "" takes i deletions.
            curr_row[0] = i

            # diagonal_val stores dp[i-1][j-1] from the previous iteration.
            # For j=1, it holds dp[i-1][0].
            diagonal_val = prev_row[0]

            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr_row[j] = diagonal_val
                else:
                    # 1 + min(insert, delete, replace)
                    # insert: dp[i][j-1] (match word1[:i] with word2[:j-1], then insert word2[j-1])
                    # delete: dp[i-1][j] (match word1[:i-1] with word2[:j], then delete word1[i-1])
                    # replace: dp[i-1][j-1] (match word1[:i-1] with word2[:j-1], then replace word1[i-1] with word2[j-1])
                    curr_row[j] = 1 + min(curr_row[j-1],   # cost for insertion
                                          prev_row[j],     # cost for deletion
                                          diagonal_val)    # cost for replacement
                
                # Update diagonal_val for the next iteration (j+1).
                # It should be the value of prev_row[j] before prev_row is updated.
                diagonal_val = prev_row[j]
            
            # The current_row becomes the prev_row for the next iteration
            prev_row = curr_row

        # The result is the last element of the final prev_row (which holds the results for word1[:m])
        return prev_row[n]
# @lc code=end

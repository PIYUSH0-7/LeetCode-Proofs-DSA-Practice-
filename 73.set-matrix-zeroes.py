#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        is_col0_zero = False
        
        # Step 1: Check if the first column needs to be zeroed
        # and use the first row and column as markers for other zeros
        for i in range(m):
            # If any element in the first column is 0, the entire first column will be zeroed later
            if matrix[i][0] == 0:
                is_col0_zero = True
            
            # Use matrix[i][0] and matrix[0][j] as markers for rows and columns
            # We start j from 1 because matrix[i][0] is used for row i's marker,
            # and matrix[0][j] for column j's marker.
            # matrix[0][0] will act as the marker for the first row.
            for j in range(1, n): 
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row i
                    matrix[0][j] = 0  # Mark column j
        
        # Step 2: Zero out cells based on the markers, iterating from bottom-right to top-left
        # This order prevents overwriting markers before they are used for dependent cells.
        # We skip column 0 here, as it's handled separately by 'is_col0_zero' and matrix[0][0]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1): # Start j from n-1 down to 1
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 3: Handle the first row based on its marker (matrix[0][0])
        # If matrix[0][0] is 0 (either it was originally 0, or some matrix[0][j] (j>0) was 0 and marked it),
        # then the entire first row needs to be zeroed.
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step 4: Handle the first column based on its flag (is_col0_zero)
        # This is done last to avoid interfering with row markers used in Step 3.
        if is_col0_zero:
            for i in range(m):
                matrix[i][0] = 0
# @lc code=end

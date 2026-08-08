#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def buildTrees(start: int, end: int) -> List[Optional[TreeNode]]:
            if (start, end) in memo:
                return memo[(start, end)]

            if start > end:
                return [None]
            
            if start == end:
                return [TreeNode(start)]

            all_possible_trees = []
            for i in range(start, end + 1):
                left_subtrees = buildTrees(start, i - 1)
                right_subtrees = buildTrees(i + 1, end)

                for left_node in left_subtrees:
                    for right_node in right_subtrees:
                        current_root = TreeNode(i)
                        current_root.left = left_node
                        current_root.right = right_node
                        all_possible_trees.append(current_root)
            
            memo[(start, end)] = all_possible_trees
            return all_possible_trees

        return buildTrees(1, n)
# @lc code=end

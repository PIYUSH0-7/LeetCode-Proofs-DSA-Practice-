#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def get_depth(node: Optional[TreeNode]) -> int:
            depth = -1
            current = node
            while current:
                depth += 1
                current = current.left
            return depth
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if left_depth == right_depth:
            # The tree formed by 'root' and its 'left_subtree' is a perfect binary tree
            # of depth 'left_depth'. Its total nodes count as 2^(left_depth + 1).
            # Recursively count nodes in the right subtree.
            return (1 << (left_depth + 1)) + self.countNodes(root.right)
        else: # left_depth > right_depth, as guaranteed by complete tree property
            # The tree formed by 'root' and its 'right_subtree' is a perfect binary tree
            # of depth 'right_depth'. Its total nodes count as 2^(right_depth + 1).
            # Recursively count nodes in the left subtree.
            return (1 << (right_depth + 1)) + self.countNodes(root.left)
# @lc code=end

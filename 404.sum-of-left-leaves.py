#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, is_left_child):
            if not node:
                return 0
            
            if is_left_child and not node.left and not node.right:
                return node.val
            
            left_subtree_sum = traverse(node.left, True)
            right_subtree_sum = traverse(node.right, False)
            
            return left_subtree_sum + right_subtree_sum

        return traverse(root, False)
# @lc code=end

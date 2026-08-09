#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        first_node = None
        second_node = None
        prev_node = None

        def inorder_traversal(node):
            nonlocal first_node, second_node, prev_node

            if not node:
                return

            inorder_traversal(node.left)

            if prev_node and node.val < prev_node.val:
                if not first_node:
                    first_node = prev_node
                second_node = node
            
            prev_node = node

            inorder_traversal(node.right)

        inorder_traversal(root)
        first_node.val, second_node.val = second_node.val, first_node.val
# @lc code=end

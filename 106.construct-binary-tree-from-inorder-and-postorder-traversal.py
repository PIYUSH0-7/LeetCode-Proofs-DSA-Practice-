#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index_inorder = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_index_inorder + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index_inorder], postorder)

        return root
# @lc code=end

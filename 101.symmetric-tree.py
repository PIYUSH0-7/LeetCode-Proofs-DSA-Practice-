#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return (node1.val == node2.val and
                    is_mirror(node1.left, node2.right) and
                    is_mirror(node1.right, node2.left))
        
        return is_mirror(root, root)
# @lc code=end

#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
        
        return build_bst(0, len(nums) - 1)
# @lc code=end

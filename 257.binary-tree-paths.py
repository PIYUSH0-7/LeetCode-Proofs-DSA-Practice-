#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []

        def dfs(node, current_path_string):
            if not node:
                return

            new_path_segment = str(node.val)
            if not current_path_string:
                path_so_far = new_path_segment
            else:
                path_so_far = current_path_string + "->" + new_path_segment

            if not node.left and not node.right:  # Leaf node
                all_paths.append(path_so_far)
                return

            dfs(node.left, path_so_far)
            dfs(node.right, path_so_far)

        dfs(root, "")
        return all_paths
# @lc code=end

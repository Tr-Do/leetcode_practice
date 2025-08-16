# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.max_depth_seen = -1

        def dfs(node, depth):
            if not node:
                return
            if depth > self.max_depth_seen:
                self.res.append(node.val)
                self.max_depth_seen = depth
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return self.res
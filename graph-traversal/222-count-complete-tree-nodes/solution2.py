# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countN(root):
            if not root:
                return 0
            count = 1
            if root.left:
                count += countN(root.left)
            if root.right:
                count += countN(root.right)
            return count
        return countN(root)
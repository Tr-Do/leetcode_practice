# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftD(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d
        def rightD(node):
            d = 0
            while node:
                node = node.right
                d += 1
            return d
        if not root:
            return 0
        ld = leftD(root)
        rd = rightD(root)
        if ld == rd:
            return 2**ld - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
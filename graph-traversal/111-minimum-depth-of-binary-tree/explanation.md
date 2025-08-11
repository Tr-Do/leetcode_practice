# Problem
Given a binary tree, find its minimum depth.

# What went wrong:
- Not add 1 in Null child cases

# Approach:
- if root is None, return 0
- if root.left is None, return 1 + self.minDepth(root.right)
- The opposite for right
- return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Time complexity:
O(n)
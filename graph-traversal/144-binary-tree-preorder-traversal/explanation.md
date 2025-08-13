# Problem
Given the root of a binary tree, return the preorder traversal of its nodes' values.

# What went wrong:
- Confuse the order with in order traversal

# Approach:
- if root is None, return []
- return [root.value] + self.preorder(root.left) + self.preorder(root.right)

# Time complexity:
O(n) : n is number of nodes
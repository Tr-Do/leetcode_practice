# Problem
Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Approach:
- if not root, return []
- return recursive root.left + recursive root.right + root.value

# Time complexity:
O(n) : n is number of nodes
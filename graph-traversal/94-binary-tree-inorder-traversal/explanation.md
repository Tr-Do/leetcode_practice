# Problem
Given the root of a binary tree, return the inorder traversal of its nodes' values.

# What went wrong:
- Unfamiliar with tree traversal algorithm
- Concantenate string with list

# Approach:
- If root is empty, return []
- else return self.method(root.left) + [root.value] + self.method(root.right)

# Insight:
- Self is used inside a class

# Time complexity:
O(n) - n is total number of nodes

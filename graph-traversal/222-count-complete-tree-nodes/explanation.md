# Problem
Given the root of a complete binary tree, return the number of the nodes in the tree.
Design an algorithm that runs in less than O(n) time complexity.

# What went wrong:
- Not initialize variable before counting
- Implement algorithm with O(n) = n
- Not distinguish between complete and perfect binary tree

# Approach:
- if root is None, return 0
- Check height of both sides, right and left. If they have the same height, the total nodes is 2**height - 1
- Otherwise, the total nodes is 1 + self.function(root.left) + self.function(root.right)

# Key insight:
- Traverse either left or right side of a COMPLETE binary tree has O(log n)

# Time complexity:
O(log n)^2
# Problem
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# What went wrong:
- Unfamiliar with depth first search algorithm

# Approach:
- Check the root, return 0 if empty
- Expand left search with self.maxDepth(root.left)
- Do the same for right
- Return max(left_depth, right_depth) + 1

# Insight:
- Self is an instance, can use method, function
- Root is a node, can use attribute
- Return +1 because 1 is counted for the current node

# Time complexity:
O(n) - n is number of nodes in the tree

# Space complexity:
O(h) - h is the height of the tree
# Problem
Given a binary tree, determine if it is height-balanced.

# What went wrong:
- Unfamiliar with depth first search algorithm

# Approach:
- Initialize a helper function with the following:
- if root is None, return 0
- left = function(root.left), if left == -1 return -1
- Same for right
- if abs(left-right) > 1, return -1
- return max(left,right) + 1
- Outside function: function(root) != -1

# Time complexity:
O(n) - n is number of nodes in the tree
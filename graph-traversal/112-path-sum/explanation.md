# Problem
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# What went wrong:
- Return tuple: root.left, targetSum, s instead of calling helper function
- Return 0 instead of False

# Approach:
- Define dfs(node, s, targetSum)
- if node is None, return False
- s += node.val
- if node is a leaf(without left and right), compare s with targetSum
- return function(node.left, s, targetSum) or function(node.right, s, targetSum)
- Outside helper function, call the helper function and pass variable to it

# Time complexity:
O(n) : n is number of nodes

# Space complexity:
O(h) : h is the height of binary tree
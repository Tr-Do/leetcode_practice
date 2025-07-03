# Problem
Given the root of a binary tree, invert the tree, and return its root.

# What went wrong:
- Incorrect assumption only root has root attribute
- Incorrectly implemented recursive

# Approach:
- Check if the binary is empty
- If not, root.left, root.right = root.right, root.left (swap left node and right node of current node)
- self.invertTree(root.left) 
- self.invertTree(root.right) (recursive for its left and right node )
- return root

# Time complexity:
O(n): n is the number of nodes - each node is visited once
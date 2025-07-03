# Problem
Given the root of a binary tree, invert the tree, and return its root.

# What went wrong:
- Incorrect implementation of stack
- Misunderstanding of pop and reference impact

# Approach:
- Check if the binary is empty
- Assign stack pointer to root
- while stack, node = stack.pop(), node.left,node.right=node.right,node.left (pop the node out then swap left with right, pop does not affect the reference but swap does)
- if node.left, stack.append(node.left) (append the children node back to stack for processing)
- if node.right, stack.append(node.right)

# Time complexity:
O(n): n is the number of nodes - each node is visited once
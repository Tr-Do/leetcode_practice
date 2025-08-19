# Problem
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

# What went wrong:
- Misunderstand the question
- Not apply the recursive condition in the return

# Approach:
- Apply base case: both root empty, return True; either empty, or both root value are different, return False
- Return recursive function:  a.left,b.left and a.right,b.right or a.left,b.right and a.right,b.left

# Time complexity:
O(n) : n is number of nodes
# Problem
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

# What went wrong:
- Use builtin Python function slicing, creating a new list and violating the constraint
- Assigned s = s[::-1], rebind the variable instead of modifying it

# Approach:
- Used 2 pointers: 1 starts from the beginnning, 1 starts from the end
- Swap the elements at 2 pointers, move them towards each other until they meet

# Time complexity:
O(n): n is the length of the array, each element is passed once

# Space complexity:
O(1): no extra data structures is used
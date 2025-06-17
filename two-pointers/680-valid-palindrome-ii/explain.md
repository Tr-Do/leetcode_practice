# Problem
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# What went wrong:
- Overwritter pointer values in helper function, ignored original range
- Not return value at the end

# Approach:
- Used 2 pointers: 1 starts from the beginnning, 1 starts from the end
- Upon mismatch, skip left or right and check if substring is a palindrome

# Time complexity:
O(n)

# Problem
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# What went wrong:
- Used wrong pointer when comparing characters

# Approach:
- Initialize i = 0
- Loop through t, increase i by 1 if when there is a match and i < len(s)
- return i == len(s)

# Time complexity:
O(n) : n is length of t

# Space complexity:
O(1)
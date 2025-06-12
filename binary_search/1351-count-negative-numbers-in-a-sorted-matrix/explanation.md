# Problem
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# What went wrong:
- Used len(arr)-l-1 instead of len(arr)-l

# Approach:
- Binary search to find the first negative number

# Time complexity:
O(m log n)
# Problem
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# What went wrong:
- Swapped the current element with the last element, increase i without checking -> skipped elements
- Use static upper bound for the loop instead of dynamically adjusting array

# Approach:
- Use 2 pointers: i scans from start, n tracks shrinking the array end

# Time complexity:
O(n)
# Problem
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# What went wrong:
- Attempted bidirectional traversal -> more complexity and out-of-bound issues
- Compare nums[i] with nums[i+1] without boundary check
- Mark duplicate with wrong value ('_')

# Approach:
- Use 2 pointers: i reads elements from index 1 to end, k tracks position to overwite
- At each step, compare nums[i] with nums[i-1]

# Time complexity:
O(n)
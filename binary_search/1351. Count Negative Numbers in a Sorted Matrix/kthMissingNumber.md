# Problem
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

# What went wrong:
- Solved it using brute force instead of binary search
- Could not derive key insight 'arr[mid] - (mid+1)'

# Approach:
- Find how many missing numbers: arr[mid] - (mid+1)
- Perform binary search to find index left such that arr[left] - (left+1) >= k
- There are 'left' elements in the array before k
- The kth missing number is k+left

# Time complexity:
O(log n)
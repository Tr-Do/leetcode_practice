# Problem
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Approach:
- Import heapq
- Negate all values in list
- Turn the list into heap
- Loop in range k, assign x to the number popped by heap
- return -x

# Time complexity:
O(logn)
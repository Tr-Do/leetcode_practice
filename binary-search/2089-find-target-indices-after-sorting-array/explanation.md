# Problem
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# What went wrong:
- Used len(arr) instead of len(arr)-1
- Overcomplicate by using nested condition

# Approach:
- Use binary search to find the target range using lower bound and upper bound
- Used nums[mid]<target to find the range(lower bound)
- Used nums[mid]<=target to get the first index to the right of that range(upper bound)
- Used right=len(nums) and right=mid in finding range instead of right=len(nums)-1 and right=mid-1 in finding exact match

# Time complexity:
O(n log n)
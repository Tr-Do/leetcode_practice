# Problem
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# What went wrong:
- Failed to construct a monotonic stack
- Stack logic did not enforce correct pop conditions
- Mapping was incomplete, missed key pops
- Leftover stack elements were not explicitly defaulted to -1

# Approach:
- Implement stack and hash map
- Trace push/pop mechanics
- Pop while stack[-1] < current

# Time complexity:
O(n) for scanning nums2
O(m) for iterating nums1
Total: O(n+m)

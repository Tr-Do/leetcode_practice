# Problem
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# What went wrong:
- Default to front to back merge logic, leading to overwritten in nums1

# Approach:
- Reverse two-pointer from end of both arrays into the end of nums1

# Time complexity:
O(m+n)
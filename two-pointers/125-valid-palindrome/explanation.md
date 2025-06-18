# Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# What went wrong:
- Default to front to back merge logic, leading to overwritten in nums1

# Approach:
- Reverse two-pointer from end of both arrays into the end of nums1

# Time complexity:
O(m+n)
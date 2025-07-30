# Problem
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# What went wrong:
- Incorrectly implemented sliding window method

# Approach:
- Check if k <= 1 => return 0
- Initiate left, result = 0, product = 1
- Loop through the array
- On the right side, the number keeps multiplying to current product
- On the left side, keep dividing if product >= k
- Result += right - left + 1 at the end of the iteration
- Return result

# Time complexity:
O(n)
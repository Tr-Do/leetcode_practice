# Problem
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# What went wrong:
- Lack of familiarity with sliding window method
- Implemented brute force, TLE

# Approach:
- current_sum = first sum of k elements
- max_sum = current_sum
- Iterate through the array, starting from k to len(nums)
- As the iteration moves forward, add nums[i] and subtract nums[i-k]
- Update max_sum using max() function
- Return the max_sum/k

# Time complexity:
O(n)
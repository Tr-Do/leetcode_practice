# Problem
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# What went wrong:
- Not implement Counter
- Use wrong heap tuple

# Approach:
- Import heapq, counter
- Use counter to count the frequency of numbers in the list, assign to count
- Initialize empty heap
- Loop through the count, use heap push, (freq, num)
- If len > k, use heappop
- Return num in heap

# Time complexity:
O(mlogn)
# Problem
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

# What went wrong:
- Did not apply hash map for optimized lookup
- Used nested loop (O(n^2))

# Approach:
- Use enumerate to iterate
- Checked for the number in hashmap and returned the pair
- If the number doesn't exist, store value as key, index as value in hashmap, go to next index

# Time complexity:
O(n)
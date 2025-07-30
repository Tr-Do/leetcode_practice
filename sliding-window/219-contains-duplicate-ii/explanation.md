# Problem
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# What went wrong:
- Redundant space to store variables
- High time complexity

# Approach:
- Initiate empty dictionary
- Loop through the array with enumerate
- Store index, value in dictionary, if the value is seen again, subtract its index with its previous index
- Return true if the value <= k
- return false outside the loop

# Time complexity:
O(n)
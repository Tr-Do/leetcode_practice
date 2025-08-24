# Problem
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# What went wrong:
- Not apply triangle inequality
- Return 0 early (inside the loop)
- Redundant complexity

# Approach:
- Sort the array in reverse (descending)
- loop through the array with range len(array) - 2
- if nums[i] < nums[i+1] + nums[i+2], return sum of 3 number
- return 0 outside the loop

# Time complexity:
O(nlogn)

# Space complexity:
O(1)
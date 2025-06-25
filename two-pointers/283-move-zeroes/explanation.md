# Problem
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# What went wrong
- Not implement 2-pointer technique effectively

# Approach:
- Create a pointer at 0, tracking where next 0 is
- Iterate throught the array, if element isn't 0, swap its position with the pointer, increment pointer by 1

# Time complexity:
O(n)
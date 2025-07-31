# Problem
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# What went wrong:
- Store subarray length in a list => space overhead
- Constraint requires O(1) space and O(n) time
- Used min(list) after iteration => another O(n) time

# Approach:
- Initiate left=0, min_l=float('inf'), total=0
- Iterate throught the array
- Total+=nums[right]
- While total>=target: min_l=min(min_l, right-left+1) total-=nums[left] left+=1
- return 0 if min_l==float('inf') else min_l

# Time complexity:
O(n)
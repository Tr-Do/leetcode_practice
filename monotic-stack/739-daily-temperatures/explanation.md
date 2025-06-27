# Problem
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead

# What went wrong:
- Failed to construct a monotonic decreasing stack
- Stack elemenst were not indices

# Approach:
- Traverse from end to start
- Use a stack to store indices of temperatures
- while stack not empty and top of stack <= current temp, pop from stack
- if stack not empty, res[i] = stack[-1] - i
- push index i to stack

# Time complexity:
O(n) 
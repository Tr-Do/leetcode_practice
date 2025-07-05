# Problem
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# What went wrong:
- Incorrect implementation of monotonic stack
- Not recognized sentinel value

# Approach:
- Create 2 sentinel values for left and right list
- In the left, iterate forwards, similar to other monotonic stacks,  heights[stack[-1]] >= heights[i] but add left[i] = stack[-1] if stack else -1
- Reset stack to save memory
- In right right, iterate backwards, similar to left, heights[i] <= heights[stack[-1]], right[i] = stack[-1] if stack else n
- Calculate rectangle width: right-left-1, subtract 1 because left and right are exclusive bounds
- Use max to find the largest area

# Time complexity:
O(n)
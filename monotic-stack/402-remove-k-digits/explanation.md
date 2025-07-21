# Problem
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# What went wrong:
- Incorrectly implement increasing monotonic stack
- Return integer 0 instead of string 0

# Approach:
- Initiate empty stack
- Iterate through the string, left to right
- while stack and stack[-1] > digit and k > 0, pop, k-=1
- Append the digit out of while loop
- stack = stack[:-k] if k>0 else stack
- Join the string, left strip 0
- return string 0 if result is empty, else return the joined string

# Time complexity:
O(n)
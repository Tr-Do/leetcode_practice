# Problem
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# What went wrong:
- Fail to implement solution from greater element i problem
- Fail to implement circular array iteration

# Approach:
- initiate greater = [-1]*n to avoid iterating in the end
- n = len(nums), for i in range(2*n), index = i%n
- The rest is similar to next greater element i solution, replace the number with index

# Time complexity:
O(n)

# Compression:
**Schema**:  
Use monotonic stack to find the next greater element; use formula of circular array for iteration

**Trapline**:
Circular array requries 2*len for iteration
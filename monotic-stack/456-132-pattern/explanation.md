# Problem
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

# What went wrong:
- Attempted to construct triplet => n^3
- Misapply monotonic stack by mixing next smaller trategy into next greater

# Approach:
- Assign second = -inf
- Traverse right to left
- At each element: compare num vs second: pattern found, then return true
- While stack not empty and stack[-1] < num -> second=pop
- Append num to stack at the end of for loop
- after the loop, return false

# Time complexity:
O(n)
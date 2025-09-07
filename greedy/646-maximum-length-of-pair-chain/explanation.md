# Problem
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.

# What went wrong:
- Sort the list according to the second element, not the first
- Not apply given condition: longest chain 

# Approach:
- Sort the list according to second element
- make cur_end = -inf
- Iterate through the list, if cur_end < start, cur_end = end, increment count
- return count

# Time complexity:
O(nlogn)

# Space complexity:
O(1)
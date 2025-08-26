# Problem
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

# What went wrong:
- Unfamiliar with heap
- Sort after each iteration, leading to n^2logn time complexity

# Approach:
- Import heapq
- Negate all numbers in the list
- heapify the list
- while len(list) > 1: x = -heappop list, y = -heapppop list
- if x!=y, heap push to list -(x-y)
- return list[0] if list, else 0

# Key insight
- sort has nlogn time complexity
- heapify has n time complexity
- heappop/heappush has logm time complexity

# Time complexity:
O(nlogn)
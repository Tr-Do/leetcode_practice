# Problem
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e., the length of the garden is n).
There are n + 1 taps located at points [0, 1, ..., n] in the garden.
Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

# What went wrong:
- Not construct correct left and right 

# Approach:
- Make a 2 dimensional array intervals from the 1 dimensional array: left = max(0, i-ranges[i]), right = min(n, i+ranges[i]), then push them into the new array
- Sort the intervals
- Initialize cur_end, next_end, i, tap = 0
- while cur_end < n, while i < len(intervals) and intervals[i][0] <= cur_end
- next_end = max(next_end, intervals[i][1])
- increment i
- outside nested while, if cur_end==next_end, return -1
- increment tap, assign cur_end = next_end
- outside while loop, return tap

# Time complexity:
O(nlogn)

# Space complexity:
O(n)
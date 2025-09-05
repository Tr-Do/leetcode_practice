# Problem
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# What went wrong:
- Sort according to their start
- Redundant function min, max
- Not remove overlap

# Approach:
- if len=1, return 0
- else, sort according to its end. 
- Initialize overlap=0, current_end=intervals[0][1]
- Iterate through interval[1:] with start, end
- if current_end > start, overlap+1
- else current_end = end
- return overlap

# Time complexity:
O(n log n): sort function takes n log n time

# Space complexity:
O(1)
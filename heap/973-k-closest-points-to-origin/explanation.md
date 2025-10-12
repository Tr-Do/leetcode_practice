# Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# What went wrong:
- Find max heap instead of min heap

# Approach:
- Import heapq
- Turn the list into heap with x*x + y*y in the beginning of heap
- Initialize empty res
- Loop k times, pop the heap each time, append x, y popped to res
- Return res

# Time complexity:
O(klogn)
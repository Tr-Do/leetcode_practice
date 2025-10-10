# Problem
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# What went wrong:
- Apply sort function on heap

# Insight:
- Heap selects the next smaller element to pop if the first elements are equal

# Approach:
- Import heapq, counter
- Use counter from collection to count the frequency of words in the string, assign to count
- Initialize empty heap 
- Loop through the count, append to list (-freq, ch)
- Heapify heap
- return heappop [1] k times

# Time complexity:
O(mlogn)
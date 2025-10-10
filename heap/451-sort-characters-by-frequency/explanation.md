# Problem
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

# What went wrong:
- Use string += concatenation which has O(n^2) time complexity
- Use wrong syntax for Counter

# Approach:
- Import heapq, counter
- Use counter from collection to count the frequency of characters in the string, assign to count
- Initialize empty heap, empty piece 
- Loop through the count, use append to list (-freq, ch)
- Heapify heap
- While heap: a, b = heappop, piece.append(-a)*
- Return ''.join(piece)

# Time complexity:
O(nlogn)
# Problem
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# What went wrong
- Used incorrect slicing leading to wrong result and errors
- Used redundant condition

# Approach:
- Split the string into blocks by 2k characters
- Reverse the first k characters in each block
- assign arr[i] = new string instead of for i in arr and i = new string

# Time complexity:
O(n)
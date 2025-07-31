# Problem
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# What went wrong:
- Append i instead of i-len_p+1

# Approach:
- Compare 2 string lengths, return [] if len(s) < len(p)
- Slide s len(p) character, apply Counter to p and the slice, res.append(0) if it's a match
- Iterate through the string
- Left = s[i-len(p)], right = s[i]
- Decrement and increment the counter at left and right as the iteration moves forward
- Remove counter = 0 from the dictionary
- Compare the slice with p in the loop, if it's a match, res.append(i-len_p+1)
- Return res at the end of the method

# Time complexity:
O(n)
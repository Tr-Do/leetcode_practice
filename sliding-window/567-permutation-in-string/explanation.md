# Problem
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

# What went wrong:
- Unaware of counting tool (Counter)
- Not implement fixed-length sliding window
- Mutated s1 without reset

# Approach:
- Compare 2 string lengths, return False if len(s1) > len(s2)
- Slide s2 len(s1) character, apply Counter to s1 and the slice, return True if it's a match
- Iterate through the string
- Left = s2[i-len(s1)], right = s2[i]
- Decrement and increment the counter at left and right as the iteration moves forward
- Remove counter = 0 from the dictionary
- Compare the slice with s1 in the loop, return True if there's a match
- Return False at the end of the method

# Time complexity:
O(n)
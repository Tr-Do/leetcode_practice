# Problem
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# What went wrong:
- Implement brute force sliding window

# Approach:
- Initialize hash map of frequency for each character
- As the pointer moves to the right, increase the count of each character
- While all 3 character exists, the total substring is len-right
- When moving the left pointer to the right, decrease the count of accoridng character, left +=1

# Time complexity:
O(n)
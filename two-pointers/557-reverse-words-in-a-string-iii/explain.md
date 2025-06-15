# Problem
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# What went wrong:
- Used two pointers to reverse characters around each space individually instead of reversing each complete word

# Approach:
- Used split function (split splits the string at the space)
- Reverse the word and use and join function to join all words to one string

# Time complexity:
O(n)

# Space complexity:
O(n)
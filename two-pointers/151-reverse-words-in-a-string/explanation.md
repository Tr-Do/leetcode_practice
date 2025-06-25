# Problem
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

# What went wrong
- Used regex -> Overhead

# Approach:
- Used split function to split the words by space
- Used join function to connect the word in reverse by space

# Time complexity:
O(n)
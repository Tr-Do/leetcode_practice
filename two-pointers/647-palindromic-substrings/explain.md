# Problem
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

# What went wrong:
- Did not recognize all valid center (odd and even)

# Approach
- Palindromes grow from the middle. Try every middle—character or gap
- Total palindromes can have from a string: 2n - 1 (n characters + n-1 gap
- Iterate through 2n - 1 . Expand outwards while characters match

# Complexity
O(n^2)
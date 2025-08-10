# Problem
Given an integer x, return true if x is a palindrome, and false otherwise.

# What went wrong:
- Not implement digit-reversal algorithm

# Approach:
- if x < 0, return False
- Initialize rev = 0, a = x
- else, while x > 0, digit = x%10 (get the last digit), rev = rev*10 + digit, x //= 10
- return rev == a

# Time complexity:
O(log x)
# Problem
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

# What went wrong:
- Started with left = 0 instead of left = 1
- While condition is left < right instead of left <= right
- Find first True -> lower bound

# Approach:
- Use binary search over [1, num]
- Use a variant of binary search instead of relying on formula of upper bound and lower bound search

# Time complexity:
O(log n)
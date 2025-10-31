# Problem
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

# What went wrong:
- Handle edge case incorrectly

# Approach:
- if n < 2, return n
- Use fibonacci formula, initialize k = [0]*(n+1)
- k[1]=1 , k[2]=2
- loop from 3 to n since n is exclusive, k[i] = k[i-1] + k[i-2]
- return k[n-1]

# Time complexity:
O(n)
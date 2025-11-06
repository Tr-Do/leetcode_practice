# Problem
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

# What went wrong:
- Implement fibonacci algorithm instead of tribonacci
- Miss edge case

# Approach:
- if n is 0 return 0, if 1 or 2, return 1
- dp=[0]*(n+1), inclusive, dp[1], dp[2]=1,1
- loop from 3 to n+1, dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
- return dp[n]

# Time complexity:
O(n)
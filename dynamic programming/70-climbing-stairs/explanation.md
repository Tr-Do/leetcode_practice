# Problem
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# What went wrong:
- Not enough time
- Miss edge case

# Approach:
- if n <= 2, return n
- Use fibonacci formula, initialize k = [0]*(n+1)
- k[1]=1 , k[2]=2
- loop from 3 to n+1 since n is inclusive, k[i] = k[i-1] + k[i-2]
- return k[n] 

# Time complexity:
O(n)
# Problem
You are given an integer array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount

# What went wrong:
- Misunderstood that stack needs to be monotonic
- Use values instead of indices in the stack

# Approach:
- Use a stack to store indices of prices
- while stack not empty and top of stack >= current price, pop from stack, result=prices[j]-prices[i]
- push index i to stack

# Time complexity:
O(n) 
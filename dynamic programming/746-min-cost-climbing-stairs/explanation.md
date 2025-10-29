# Problem
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

# What went wrong:
- Not enough time

# Approach:
- prev2=cost[0], prev1=cost[1]
- move forward from 2 to end of array
- cur = current cost + smaller one of previous 2 steps
- prev2, prev1 = prev1, cur
- the top is 1 step away from the last step=> take min of last 2 values
- return min(prev2, prev1)

# Time complexity:
O(n)
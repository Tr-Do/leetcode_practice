# Problem
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# What went wrong:
- Solve with wrap-around iteration
- Use tank = gas[i] - cost[i] instead of tank += gas[i]-cost

# Approach:
- if sum of gas < sum of cost, return -1
- Initialize start, tank = 0
- Iterate through len(gas), tank += gas[i]-cost[i]
- if tank < 0, start = i+1, tank = 0
- return start

# Time complexity:
O(n)

# Space complexity:
O(1)
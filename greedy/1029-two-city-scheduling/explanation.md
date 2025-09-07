# Problem
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
 
# What went wrong:
- Overcomplicate the solution (use dict instead of sorting list)

# Approach:
- Sort costs ascending x[0] - x[1]
- Loop first half of costs, add costs[i][0] to total
- Loop second half, add costs[i][1] to total
- return total

# Time complexity:
O(nlogn)

# Space complexity:
O(1)
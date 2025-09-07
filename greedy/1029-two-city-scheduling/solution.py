class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        n = len(costs) // 2
        costs.sort(key = lambda x:x[0] - x[1])
        for i in range(n):
            total += costs[i][0]
        for i in range(n, 2*n):
            total += costs[i][1]
        return total
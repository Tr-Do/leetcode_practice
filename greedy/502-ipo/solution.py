import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)
        curr = w
        for _ in range(k):
            while i < n and projects[i][0] <= curr:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            curr += -heapq.heappop(max_heap)
        return curr

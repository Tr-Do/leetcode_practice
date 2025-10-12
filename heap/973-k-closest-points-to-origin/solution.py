import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
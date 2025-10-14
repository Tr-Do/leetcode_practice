import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        res = [0] * len(heap)
        rank = 1
        prize = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        while heap:
            score, idx = heapq.heappop(heap)
            if rank <= 3:
                res[idx] = prize[rank-1]
            else:
                res[idx] = str(rank)
            rank += 1
        return res
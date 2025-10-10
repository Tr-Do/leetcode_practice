import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        piece = []
        count = Counter(s)
        heap = [(-frq, ch) for ch, frq in count.items()]
        heapq.heapify(heap)
        while heap:
            a, b = heapq.heappop(heap)
            piece.append(-a*b)
        return ''.join(piece)
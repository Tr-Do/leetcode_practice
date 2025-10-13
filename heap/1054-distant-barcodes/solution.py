import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        heap = [(-cnt, val) for val, cnt in freq.items()]
        heapq.heapify(heap)
        
        res = []
        prev = (0, None)  # (remaining count, value)
        
        while heap:
            cnt, val = heapq.heappop(heap)
            res.append(val)
            cnt += 1  # because stored as negative

            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (cnt, val)
        return res

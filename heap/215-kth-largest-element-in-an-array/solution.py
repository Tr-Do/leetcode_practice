import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        x=0
        for i in range(k):
            x= heapq.heappop(nums)
        return -x
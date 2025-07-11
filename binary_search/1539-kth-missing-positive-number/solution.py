class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l<=r:
            m = (l+r)//2
            miss = arr[m]-(m+1)
            if miss < k:
                l = m +1
            else:
                r = m -1
        return k+l

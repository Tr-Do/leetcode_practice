class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        def s(arr, k):
            l, r = 0, len(arr)-1
            while l <= r:
                m = (l+r) // 2
                if arr[m] == k:
                    return m
                elif arr[m] < k:
                    l = m + 1
                else:
                    r = m - 1
            return None

        bobSizes.sort()
        aliceSizes.sort()
        
        bobS = sum(bobSizes)
        aliceS = sum(aliceSizes)
        delta = (bobS - aliceS) // 2

        for a in aliceSizes:
            b = a + delta
            if s(bobSizes, b) is not None:
                return [a, b]
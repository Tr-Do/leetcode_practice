class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary(arr):
            l,r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if arr[m] == 1:
                    l = m+1
                else:
                    r = m-1
            return l
        countS = []
        for i, num in enumerate(mat):
            count = binary(num)
            countS.append((count, i))
        countS.sort()
        return [countS[i][1] for i in range(k)]
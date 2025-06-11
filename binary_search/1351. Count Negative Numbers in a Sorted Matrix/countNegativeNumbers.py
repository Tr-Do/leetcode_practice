class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def predicate(arr):
            l,r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if arr[m] < 0:
                    r = m-1
                else:
                    l = m+1
            return len(arr)-l
        return sum(predicate(i) for i in grid)
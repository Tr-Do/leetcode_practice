class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def need(s):
            total=0
            split=1
            for i in nums:
                if total+i>s:
                    total=i
                    split+=1
                else:
                    total+=i
            return split
        low,high=max(nums),sum(nums)
        while low<high:
            mid=(low+high)//2
            if need(mid)>k:
                low=mid+1
            else:
                high=mid
        return low
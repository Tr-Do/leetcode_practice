class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        def bileft(arr,s):
            left,right = 0, len(arr)
            while left < right:
                mid = (left+right)//2
                if arr[mid] < s:
                    left = mid +1
                else:
                    right = mid
            return left
        def biright(arr, s):
            left, right = 0, len(arr)
            while left < right:
                mid = (left+right)//2
                if arr[mid] <= s:
                    left = mid +1
                else:
                    right = mid
            return left
        left = bileft(nums,target)
        right = biright(nums, target)
        if left == right:
            return []
        else:
            return list(range(left,right))

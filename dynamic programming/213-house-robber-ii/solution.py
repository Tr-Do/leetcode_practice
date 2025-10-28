class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        def rob(arr):
            prev2, prev1 = 0,0
            for x in arr:
                curr = max(prev1, prev2+x)
                prev2, prev1 = prev1, curr
            return prev1
        return max(rob(nums[1:]), rob(nums[:-1]))
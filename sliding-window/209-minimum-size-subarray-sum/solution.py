class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_l = min(min_l, right-left+1)
                total -= nums[left]
                left += 1
        return 0 if min_l == float('inf') else min_l
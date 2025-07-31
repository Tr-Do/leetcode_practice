class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = []
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_l.append(right-left+1)
                total -= nums[left]
                left += 1
        return 0 if not min_l else min(min_l)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curent_sum = sum(nums[:k])
        max_sum = curent_sum
        for i in range(k, len(nums)):
            curent_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curent_sum)
        return max_sum/k
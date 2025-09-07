class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        sub_sum = 0
        sub = []
        for x in nums:
            sub.append(x)
            sub_sum += x
            total -= x
            if sub_sum > total:
                return sub
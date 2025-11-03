class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        if not nums or max(nums) > target:
            return False

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for s in range(target, x - 1, -1):
                if dp[s - x]:
                    dp[s] = True
            if dp[target]:
                return True
        return dp[target]

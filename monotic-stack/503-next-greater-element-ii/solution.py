class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        greater = [-1]*n
        for i in range(2*n):
            c = nums[i%n]
            while stack and nums[stack[-1]] < c:
                greater[stack.pop()] = c
            if i < n:
                stack. append(i)
        return greater
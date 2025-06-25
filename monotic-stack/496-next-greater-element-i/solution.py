class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                smaller = stack.pop()
                greater[smaller] = i
            stack.append(i)
        for i in stack:
            greater[i] = -1
        return [greater[i] for i in nums1]
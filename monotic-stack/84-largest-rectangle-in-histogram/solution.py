class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            stack = []
            n = len(heights)
            left = [-1] * n
            right = [n] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            stack = []
            for i in reversed(range(n)):
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                right[i] = stack[-1] if stack else n
                stack.append(i)
            max_a = 0
            for i in range(n):
                width = right[i] - left[i] - 1
                area = heights[i] * width
                max_a = max(max_a, area)
            return max_a
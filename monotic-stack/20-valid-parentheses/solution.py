class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'{':'}', '[':']', '(':')'}
        for char in s:
            if char in dic:
                stack.append(dic[char])
            else:
                if not stack or stack[-1] != char:
                    return False
                stack.pop()
        return not stack
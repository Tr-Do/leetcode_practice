class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(b/a))

        return stack[0]
def removeDuplicateLetters(s: str) -> str:
    last = {ch: i for i, ch in enumerate(s)}
    in_stack = {ch: False for ch in 'abcdefghijklmnopqrstuvwxyz'}
    stack = []
    for i, ch in enumerate(s):
        if in_stack[ch]:
            continue
        while stack and ch < stack[-1] and last[stack[-1]] > i:
            in_stack[stack.pop()] = False
        stack.append(ch)
        in_stack[ch] = True
    return ''.join(stack)
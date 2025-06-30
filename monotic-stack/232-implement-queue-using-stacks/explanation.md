# Problem
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# What went wrong:
- Incorrect assumption stack behavior
- Tried to simulate queue with a single stack
- Misued python constructs (pop(0), slicing, and len(self)), which are not allowed
- Mishandled pop() and peek() on empty queue

# Approach:
- Used stack_in for push operation
- Used stack_out for peek, pop operation
- Push: use append method
- Pop: call peek to ensure the correct order, then pop from stack_out
- Peek: if stack_out is empty, move all elements from stack_in to stack_out, then return stack_out[-1]
- Empty: return not stack_in and not stack_out

# Time complexity:
push: O(1)
empty: O(1)
peek, pop: amortized O(1), worst-case: O(n)
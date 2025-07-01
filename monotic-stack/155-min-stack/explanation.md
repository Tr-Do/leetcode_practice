# Problem
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

# What went wrong:
- Loop through the stack, making O(n) instead of O(1)

# Approach:
- Create 2 empty stacks
- Push: append val to stack1, if not stack2 or stack2[-1] >= val, stack2.append(x)
- Pop: x = stack1.pop(), if x == stack2[-1], then stack2.pop()
- Top: return stack1[-1]
- getMin: return stack2[-1]

# Time complexity:
O(1)

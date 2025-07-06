# Problem
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

# What went wrong:
- Incorrect implementation of isdigit
- Misunderstanding the order when popping the element
- Return the stack instead of the element

# Approach:
- create empty stack, iterate through the array
- if i.lstrip('-').isdigit() then append to stack (isdigit fail to detect negative number)
- if i is not digits, pop out 2 numbers and do calculations
- For - and / , right pop - or / left pop, then int() division to truncate towards 0

# Time complexity:
O(n)

# Compression
**Schema**: 
Use monotonic stack to keep the numbers and pop them out for calculation

**Trapline**:
The input is string, need to check if it's a digit and strip out negative sign before doing that; truncate towards 0 requires int, // truncates towards negative infinity
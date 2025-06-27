# Problem
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations

# What went wrong:
- Used non-existent method `.isnum()` to check if the input is a number
- Used `str.isdigit()` without handling negative numbers (isdigit only returns True for positive numbers)

# Approach:
- Iterate through the list
- if op.lstrip('-').isdigit(), convert to int and push to stack
- stack.pop() for C
- Use stack[-1] for "D", stack[-1] + stack[-2] for "+"
- Return sum(stack)

# Time complexity:
O(n) 
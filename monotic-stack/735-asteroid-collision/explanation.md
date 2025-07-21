# Problem
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# What went wrong:
- Incorrectly treated this as a monotonic stack problem - it is not
- Misunderstanding spatial relationship: stack[-1] is prior in both position and time

# Approach:
- Initiate empty stack
- Iterate through the array
- while stack and stack[-1]>0 and a<0 (condition for collision)
- if stack[-1] > -a: break (exit while loop)
- elif stack[-1] < -a: stack.pop, continue
- else: stack.pop, break (exit while loop)
- while else: push asteroid to stack
- return stack

# Time complexity
O(n) 

# Insight:
- Current asteroid always appears later in the array
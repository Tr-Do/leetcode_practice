# Problem
pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).

# What went wrong:
- Return result after loop instead of inside the conditional block
- Called guess multiple times during each iteration, increasing runtime

# Approach:
- Use binary search over [1, n]
- Store guess(mid) in a variable and compare the value in each loop

# Time complexity:
O(log n)
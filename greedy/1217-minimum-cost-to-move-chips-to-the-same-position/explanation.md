# Problem
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

# What went wrong:
- Not fully understand the question
- Add position to even, odd in the loop instead of incrementing by 1

# Approach:
- Intialize odd, even = 0
- Move by 2 cost 0, move by 1 cost 1 => odd to odd, even to even is free to move, odd to even, even to odd costs 1
- Move all odds to the same position, all even to the same position
- The minimum cost is the min between even and odd

# Time complexity:
O(n)

# Space complexity:
O(1)
# Problem
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# What went wrong:
- Not add 2 0 paddings on both sides
- Not return early when the result is true

# Approach:
- Make a new bed with 0 on each side
- Iterate through the bed, range from 1 to len(newBed)-1
- if before, current and after position has value 0, assign the current to 1, count += 1
- if count >= n, return True
- outside loop, return count >= n

# Time complexity:
O(n)

# Space complexity:
O(1)
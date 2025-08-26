# Problem
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children

# What went wrong:
- Assign candy to the wrong side during right to left interation

# Approach:
- Initialize [1] * len(ratings) to assign 1 candy to all children
- Iteration from left to right, increment candy to the neighbor by 1 if the neighbor's rating is higher
- Iteration from right to left, update left index with neighbor's finanlized candy
- return sum(candy)

# Time complexity:
O(n)
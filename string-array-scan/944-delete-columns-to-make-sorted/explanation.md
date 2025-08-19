# Problem
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete

# What went wrong:
- Append the characters to stack and sort stack

# Approach:
- Initialize col=0
- Apply brute force method, in the nested loop, range is len-1
- if strs[j][i] > strs[j+1][i]: col+=1 break
- return col

# Time complexity:
O(m x n)
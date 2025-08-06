# Problem
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# What went wrong:
- Incorrectly handled sorting by soldier count and index
- Didn't construct (soldier, index) tuple/list correctly

# Approach:
- Use binary search as predicate to count number of soldiers per row
- Use enumerate to pair soldier count with index
- Sort the tuple, tuple is faster than list in terms of time complexity

# Time complexity:
Count soldier: O(m log n)
Sort pairs: O(m log m)
Total: O(m log n + m log m)
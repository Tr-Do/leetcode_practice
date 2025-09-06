# Problem
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

# What went wrong:
- Assign 1 cookie to more than 1 child

# Approach:
- Sort 2 lists
- Iterate through 2 lists at the same time with while loop
- If the cookie satisfies the child, move to next cookie and next child, increment count
- If not, move to the next cookie
- return count

# Time complexity:
O(nlogn)
# Problem
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
must not use any built-in exponent function or operator

# What went wrong:
- Used binary search without aligning return logic to predicate
- Returned left - should use return right to get the last True

# Approach:
- Find the last True -> upper bound

# Key insights:
- The problem of finding k such that k^2 ≤ x
- Return matches predicate boundary, not midpoint
- Template logic must follow predicate, not replace it

# Time complexity:
O(log n)
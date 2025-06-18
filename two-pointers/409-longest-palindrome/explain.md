# Problem
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# What went wrong
- Misapplied sorting, reversing, and character reassignment that don't relate
- No knowledge of basic frequency counting logic

# Approach:
- Count the frequency of each character using hash map
- For each count:
    + Add even number to count
    + Track if any has odd count
- If at least 1 odd exists, add 1 to total

# Time complexity:
O(n) , 1 pass to count, 1 pass to compute
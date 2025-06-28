# Problem
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

# What went wrong:
- Combine the condition, stack is none empty and char =='#' => stack.pop()
- Append # to the stack

# Approach:
- Split the condition, if char=='#' then if stack
- Else append all characters, except #

# Time complexity:
O(n+m): string s and t
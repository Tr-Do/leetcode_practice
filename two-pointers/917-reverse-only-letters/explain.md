# Problem
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

# What went wrong:
- Used invalid comparison in ASCII range: a <= value <= Z
- Used isalpha instead of isalpha(), leading to incorrect evaluation, method wasn't executed

# Approach:
- Use 2 pointer method: start pointers at start and end
- Move both inward, skip non letter characters
- Swap letters in place when both are letters

# Time complexity:
O(n)
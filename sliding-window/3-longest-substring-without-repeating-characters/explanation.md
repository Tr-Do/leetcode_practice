# Problem
Given a string s, find the length of the longest substring without duplicate characters.

# What went wrong:
- Increment left pointer once when frequency > 1
- Cause duplicate in the window -> incorrect length

# Approach:
- Initalize max_len=0, defaultdict, left=0
- Iterate through the array
- Add one to the frequency of character as the right pointer moves to the right
- When frequency > 1, dict[s[left]] -= 1, left += 1
- max_len = max(max_len, right-left+1)

# Time complexity:
O(n)
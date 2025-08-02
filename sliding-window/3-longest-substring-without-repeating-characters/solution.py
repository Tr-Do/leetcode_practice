from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        dict_a = defaultdict(int)
        left = 0
        for right in range(len(s)):
            dict_a[s[right]] += 1
            while dict_a[s[right]] > 1:
                dict_a[s[left]] -= 1
                left += 1
            max_l = max(max_l, right-left+1)
        return max_l
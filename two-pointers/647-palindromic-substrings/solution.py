class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2*len(s)-1):
            left = i // 2
            right = left + (i%2)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
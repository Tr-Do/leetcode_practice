class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        l,r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return palindrome(l+1,r) or palindrome (l,r-1)
        return True
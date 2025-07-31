from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        res = []
        if len_p > len_s:
            return []
        count_s = Counter(s[:len_p])
        count_p = Counter(p)
        if count_s == count_p:
            res.append(0)
        for i in range(len_p, len_s):
            left = s[i-len_p]
            right = s[i]
            count_s[left] -= 1
            count_s[right] += 1
            if count_s[left] == 0:
                del count_s[left]
            if count_s == count_p:
                res.append(i-len_p+1)
        return res
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        end = float('-inf')
        pair = 0
        for i, j in pairs:
            if end < i:
                pair += 1
                end = j
        return pair
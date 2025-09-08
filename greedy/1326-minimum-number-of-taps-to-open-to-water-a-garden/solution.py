class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n+1):
            left = max(0, i-ranges[i])
            right = min(n, i+ranges[i])
            intervals.append((left, right))
        intervals.sort()
        cur_end, next_end, i, tap = 0,0,0,0
        while cur_end < n:
            while i <= n and intervals[i][0] <= cur_end:
                next_end = max(next_end, intervals[i][1])
                i += 1
            if cur_end == next_end:
                return -1
            tap += 1
            cur_end = next_end
        return tap
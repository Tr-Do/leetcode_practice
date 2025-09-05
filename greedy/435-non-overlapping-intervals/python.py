class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        else:
            intervals.sort(key=lambda x:x[1])
            overlap = 0
            current_end = intervals[0][1]
            for start, end in intervals[1:]:
                if current_end > start:
                    overlap += 1
                else:
                    current_end = end
        return overlap
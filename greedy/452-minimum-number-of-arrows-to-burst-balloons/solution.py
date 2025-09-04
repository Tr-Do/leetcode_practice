class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        else:
            points.sort(key=lambda x:x[1])
            arrow = 1
            current_end = points[0][1]
            for start, end in points[1:]:
                if start > current_end:
                    arrow += 1
                    current_end = end
        return arrow
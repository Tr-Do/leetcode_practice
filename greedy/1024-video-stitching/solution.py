class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        res = 0
        curr_end = 0
        next_end = 0
        i = 0
        while curr_end < time:
            while i < len(clips) and clips[i][0] <= curr_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            if next_end == curr_end:
                return -1
            res += 1
            curr_end = next_end
        return res 
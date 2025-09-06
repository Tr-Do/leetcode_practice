# Problem
You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.
Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.
We can cut these clips into segments freely.
For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.

# What went wrong:
- Not find the clip yielding max length from 0
- Not assign current_end to next_end

# Approach:
- Sort the list according to the start time
- Intialize current_end, next_end, i, res = 0
- Use nested while loop to iterate through the list, preventing starting from 0 after each resest
- while current_end < time then while current iteration < len(clips) and current clip starting time <= current_end
- next_end = max(next_end, clips[i][1]), then increment i
- Handle edge case when current_end == next_end, return -1
- return res

# Time complexity:
O(nlogn)

# Space complexity:
O(1)
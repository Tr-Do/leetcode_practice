# Problem
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

# What went wrong:
- Brute force to generate all pairs
- Return j, j instead of nums[i], nums[j]

# Approach:
- Import heapq
- heap = nums1[i] + nums2[0], i , 0 for i in range(min(len(nums1), k)): push to heap the sum of each element nums1 with the first element of nums2 and their indices
- heapify heap
- Initialize res= []
- While heap and len(res) < k: heappop, append nums[i], nums[j] into res
- if j+1 < len(nums2), j is element index of nums2
- heap push nums1[i]+ nums2[j+1], i, j+1
- outside loop: return res

# Time complexity:
O(klog(min(k, len(nums1))))
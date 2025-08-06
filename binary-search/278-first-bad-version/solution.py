# 278. First Bad Version
# Difficulty: Easy
# Time complexity: O(log n)
# Space complexity: O(1)
# URL: https://leetcode.com/problems/first-bad-version/description/?envType=problem-list-v2&envId=binary-search

def firstBadVersion(n):
    left = 1
    right = n

    while left < right:  # strictly less
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

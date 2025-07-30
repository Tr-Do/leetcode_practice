from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valu = defaultdict(list)
        for i, j in enumerate(nums):
            valu[j].append(i)
        for value in valu.values():
            value.sort()
            for index in range(len(value)-1):
                if value[index+1] - value[index] <= k:
                    return True
        return False
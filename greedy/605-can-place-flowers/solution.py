class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(bed)-1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                count += 1
                bed[i] = 1
                if count >= n:
                    return True
        return count >= n
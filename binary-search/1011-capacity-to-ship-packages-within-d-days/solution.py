class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity, days):
            day = 1
            total = 0
            for w in weights:
                if total + w > capacity:
                    day += 1
                    total = 0
                total += w
            return day <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid, days):
                right = mid
            else:
                left = mid + 1
        return left

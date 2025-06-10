class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = -1
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        if letters[result] > target:
            return letters[result]
        else:
            return letters[0]
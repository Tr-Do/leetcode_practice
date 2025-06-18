class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = [s[i:i+2*k] for i in range(0,len(s),2*k)]
        for i in range(len(arr)):
            if len(arr[i]) < k:
                arr[i] = arr[i][::-1]
            else:
                arr[i] = arr[i][:k][::-1] + arr[i][k:]
        return "".join(arr)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        result = prices[:]
        
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                result[j] = prices[j] - prices[i]
            stack.append(i)
        return result
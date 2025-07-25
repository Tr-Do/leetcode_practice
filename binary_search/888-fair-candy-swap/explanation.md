# Problem
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

# Approach:
- Compute total candies
- Compute delta: delta = (sumB - sumA) // 2
- Sort both arrays for binary search
- For each a in aliceSizes, check if b = a + delta exists in bobSizes using binary search

# Time complexity:
- Sorting 'bobSizes': O(n log n)
- for each a in aliceSizes, binary search b in bobSizes: O(m log n)
- Total: O(n log n + m log n)

# Key insights:
- Equalize the total of each array
- // returns int, / returns float
- 2(b-a) = sumB - sumA => b = a + delta
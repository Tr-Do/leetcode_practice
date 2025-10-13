# Problem
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

# What went wrong:
- Unfamiliar previous element hold technique

# Approach:
- Import heapq, counter
- Apply counter on the list, then turn it into heap with -freq, val for val, freq in barcodes
- Initialize empty req, prev=(0,None)
- while heap: freq, val = heappop(heap), req.append(val), freq+=1
- if prev[0]<0: heappush(heap, prev)
- outside if: prev=(freq, val)
- return req

# Time complexity:
O(mlogn)
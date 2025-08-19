# Problem
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

# What went wrong:
- Redundant variable 'twenty' for $20 bill

# Approach:
- Base case: if first index is not $5 bill, return False
- Iterate through the list, increment and decrement variables accoring to the bill and change
- return False if there is not enough bill
- return True outside the loop

# Time complexity:
O(n)

# Space complexity:
O(1)
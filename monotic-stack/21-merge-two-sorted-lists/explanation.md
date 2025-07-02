# Problem
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

# What went wrong:
- Incorrectly apply list property on linked list

# Approach:
- Create a dummy node
- Set tail point to dummy
- while list1 and list2, if list1.val < list2.val: tail.next = list1 list1 = list1.next (move tail's pointer to list1's node then move list1's node point to the next one)
- After that, move tail's pointer to the rest of the longer node (tail.next = list1 if list1 else list2)
- Return dummy.next since dummy.next points to the first node, dummy currently points at the assigned value

# Time complexity:
O(n)
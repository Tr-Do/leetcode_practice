class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value = []
        current = head
        while current:
            value.append(current.val)
            current = current.next
        if value == value[::-1]:
            return True
        else:
            return False

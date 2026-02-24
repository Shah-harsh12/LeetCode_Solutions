# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head and not head.next:
            return head

        fast , slow = head , head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = self.reverse(slow)
        p1 , p2 = head , second_half

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
        
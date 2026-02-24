# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional
class Solution:
    def reverse(self , head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next

        slow.next = None
        first = head

        second = self.reverse(second_half)

        dummy = ListNode(0)
        curr = dummy

        while first or second:
            if first:
                curr.next = first
                curr = curr.next
                first = first.next
            if second:
                curr.next = second
                curr = curr.next
                second = second.next

        
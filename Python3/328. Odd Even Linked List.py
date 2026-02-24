# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional
     
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = head
            even = head.next
            evenhead = even
            while even and even.next:
                odd.next = even.next
                odd = odd.next

                even.next = odd.next
                even = even.next

            odd.next = evenhead

            return head
        else:
            return head
        
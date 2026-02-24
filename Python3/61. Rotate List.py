# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional
     
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0 :
            return head
        count = 1
        temp = head
        
        while temp.next:
            temp = temp.next
            count += 1

        k = k % count

        if k == 0:
            return head
        
        no_of_nodes = count - k
        curr = head
        
        for _ in range(1 , no_of_nodes):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        temp.next = head
        
        return new_head
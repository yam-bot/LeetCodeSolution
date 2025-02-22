# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode() , ListNode() 
        ptr1 , ptr2 = dummy1, dummy2
        curr = head
        while curr:
            if curr.val >= x:
                ptr2.next = curr
                ptr2 = ptr2.next
            elif curr.val < x:
                ptr1.next = curr
                ptr1 = ptr1.next
            curr = curr.next
        ptr2.next = None
        ptr1.next = dummy2.next
        return dummy1.next
        
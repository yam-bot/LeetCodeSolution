# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        if k > length:
            k = k % length
        k = length - k
        if k == 0:
            curr.next = None
            return head
        curr = head
        for i in range(1,k):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
        


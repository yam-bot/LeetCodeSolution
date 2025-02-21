# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            if not node or not node.next:
                return node
            first = node
            second = node.next
            first.next = swap(second.next)
            second.next = first
            return second
        return swap(head)


        # 1. slow = fast.next , fast = fast.next.next
        #1  2   3   4   5   6
        #s  f  s2  f2
        #2  1  
        #      s  f
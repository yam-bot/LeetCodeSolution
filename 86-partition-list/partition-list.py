# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #6 -> 1 -> 4 ->  3 -> 2 -> 5 -> 9 -> 7
        #           ^
        #if nodeindex != 3 and node > nodevalue : return node
        #if nodeindex != 3 and node < nodevalue : return node.next
        dummy1, dummy2 = ListNode() , ListNode() 
        ptr1 , ptr2 = dummy1, dummy2
        curr ,  length = head , 1
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
        #def findpart(node,d1,d2):
        #    if not node :
        #        return
        #    node.next = findpart(node.next,d1,d2)
        #    print(node , node.next)
        #    if node.val >= x:
        #        d2.next = node
        #        d2 = d2.next
        #        #return node
        #    elif node.val < x:
        #        dummy1.next = node
        #        dummy1 = dummy1.next
        #        #return node.next
        #    print("d1",dummy1,"d2",dummy2)
        #return findpart(curr)
        
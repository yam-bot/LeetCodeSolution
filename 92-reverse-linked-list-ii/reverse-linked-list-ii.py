# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right : return head
        dummy1 ,seperateddummy, dummy2 = ListNode() , ListNode(),  ListNode()
        begin ,seperated, seperatedhead , tail = dummy1 ,seperateddummy, None, dummy2
        curr, length = head , 1
        while curr:
            if length < left:
                begin.next = curr
                begin = begin.next
            elif length > right:
                tail.next = curr
                tail = tail.next
            else:
                seperatedhead = curr if length == left else seperatedhead
                seperated.next = curr
                seperated = seperated.next
            length += 1
            curr = curr.next
        seperated.next, begin.next, tail.next = None , None, None
        print(dummy1.next)
        print(dummy2.next)
        print(begin)
        def reverse(node):
            if not node.next or not node:
                return node
            rev_head = reverse(node.next)
            node.next.next = node
            node.next = None
            seperated = node
            return rev_head
        newseperated = reverse(seperateddummy.next)
        if dummy1.next and dummy2.next:
            begin.next = newseperated
            seperatedhead.next = dummy2.next
            return dummy1.next
        elif dummy1.next:
            begin.next = newseperated
            return dummy1.next
        elif dummy2.next:
            seperatedhead.next = dummy2.next
            return newseperated
        else:
            return newseperated

                
        
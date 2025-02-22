"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class ListNode:
    def __init__(self, val: int = 0, next: 'Node' = None):
        self.val = val
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root : return root
        curr , nxt = root , root.left
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root
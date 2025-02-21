# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        repeated , visited = set() , set()
        curr = head
        while curr:
            if visited and curr.val in visited:
                repeated.add(curr.val)
            visited.add(curr.val)
            curr = curr.next
        
        stack = [None]
        def checkduplicate(node):
            if not node.next and node.val in repeated:
                return None
            elif not node.next:
                stack[-1] = node
                return node
            node.next = checkduplicate(node.next)
            #print(node.next)
            if node.val not in repeated:
                stack[-1] = node
            return stack[-1]
        return checkduplicate(head)
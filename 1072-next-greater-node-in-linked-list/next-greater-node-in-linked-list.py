# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node , ans, stack = head , [], []
        def findnextgreater(curr):
            if not curr or not curr.next:
                ans.append(0)
                stack.append(curr.val)
                return
            findnextgreater(curr.next)
            while stack and (stack[-1] <= curr.val):
                stack.pop()
            nextgreater = stack[-1] if stack else 0
            ans.append(nextgreater)
            stack.append(curr.val)
            return
        findnextgreater(node)
        return ans[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1  2  3  4  5  6  7
# sf
# 1  2  3  4  5  6  7
#    s     f  
# 1  2  3  4  5  6  7
#       s  f
# 1  2  3  4  5  6  7  N
#          s  f
# 1  2
# sf
# 1  2  N
#    s     
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head : return head
        def find_middle(llist):
            slow, fast, prev = llist , llist , None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev : prev.next = None
            return slow
        if not head.next:
            return TreeNode(head.val)
        mid = find_middle(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

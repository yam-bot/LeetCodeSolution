# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# i    fast     slow
# 1      3       3
# 2      0       2
# 3      2       0
# 4     -4      -4      

# 1      3       3
# 2      0       2
# 3     -5       0
# 4     -4      -4


# 1      3       3
# 2      0       2
# 3     -5       0
# 4      0      -4
# 5     -5      -5
# k = number of node in cycle
# m = number of nodes before cycle
# x = number of step in cycle
# q = number of loop
# m + x + kq = 2(m + x)
# kq = m + x
# m = k - x
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, cycle = head, head, False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if not cycle : return None
        slow = head
        print(fast)
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print(slow)
        return slow

    
        
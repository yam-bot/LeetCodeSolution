# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 , curr2 = l1, l2
        stack1 , stack2 = [] , []
        while curr1 or curr2:
            if curr1 : stack1.append(curr1.val)
            if curr2 : stack2.append(curr2.val)
            curr1 = curr1.next if curr1 and curr1.next else None
            curr2 = curr2.next if curr2 and curr2.next else None
        num1 , num2 = 0 , 0
        for i in range(len(stack1)-1,-1,-1):
            num1 += stack1[i] * (10 ** i)
        for i in range(len(stack2)-1,-1,-1):
            num2 += stack2[i] * (10 ** i)
        sumnum = num1 + num2
        print(num1,num2)
        numlist = [int(n) for n in str(sumnum)]
        print(numlist)
        dummy = ListNode()
        tail = dummy
        while numlist:
            n = numlist.pop()
            node = ListNode(n,None)
            tail.next = node
            tail = tail.next
        return dummy.next
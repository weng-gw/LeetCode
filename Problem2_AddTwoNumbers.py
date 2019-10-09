# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = 0
        out = ListNode(0)
        p = out
        while l1 or l2 or last:
            temp_sum = (l1.val if l1 else 0)+(l2.val if l2 else 0)+ last
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p.next = ListNode(temp_sum%10)
            last = temp_sum//10
            p = p.next
        return out.next


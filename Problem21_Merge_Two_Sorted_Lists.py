# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:         
            return l1
        if l1.val <= l2.val:
            head = l1
            p1 = l1.next 
            p2 = l2
            pnew = l1
        else:
            head = l2
            p1 = l1
            p2 = l2.next
            pnew = l2   
        while  p1 and  p2:
            if p1.val <= p2.val:
                pnew.next = p1
                pnew = pnew.next
                p1 = p1.next
            else:
                pnew.next = p2
                pnew = pnew.next
                p2 = p2.next
        if not p1:
            pnew.next = p2
        else:
            pnew.next = p1
        return head
        

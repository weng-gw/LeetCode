# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        la = 0
        lb = 0
        while pa:
            la+=1
            pa = pa.next
        while pb:
            lb+=1
            pb = pb.next
        l1,l2 = (headA,headB) if la>lb else (headB,headA)
        ahead = abs(la-lb)
        for i in range(ahead):
            l1 = l1.next
        while l1 and l2 and l1!=l2:
            l1 = l1.next
            l2 = l2.next
        return l1
        

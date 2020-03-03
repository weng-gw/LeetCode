# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        new_head = ListNode(0)
        p1 = new_head
        p2 = head
        n = 1
        while p2:
            if not p2.next:
                if n==1:
                    p1.next = p2
                    p1 = p1.next
            elif p2.next.val == p2.val:
                n+=1
            else:
                if n==1:
                    p1.next = p2
                    p1 = p1.next
                n=1
            p2 = p2.next
        p1.next=None
        return new_head.next

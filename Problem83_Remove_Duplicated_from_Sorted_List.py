# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p=head.next
        last = head
        while p:
            if p.val != last.val:
                last.next = p
                last = p
            p = p.next
        last.next = None
        return head
            



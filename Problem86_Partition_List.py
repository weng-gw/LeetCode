#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        less = ListNode(0)
        greater = ListNode(x)
        p1 = less
        p2 = greater
        while head:
            if head.val <x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head=head.next
        p1.next = None
        p2.next = None
        if less.next:
            head = less.next
            p1.next = greater.next
        else:
            head = greater.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1 = head
        head = p1.next
        prev = None
        while p1 and p1.next :
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1
            if prev:
                prev.next = p2
            else:
                head = p2
            prev = p1
            p1 = p1.next
        return head

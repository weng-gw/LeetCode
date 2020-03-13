# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n or not head:
            return head
        new_head = ListNode(0)
        new_head.next = head
        p1 = new_head
        for i in range(m-1):
            p1 = p1.next
        sub_end = p1.next
        p2 = p1.next
        prev = None
        for i in range(n-m+1):
            curr = p2
            p2 = p2.next
            curr.next = prev
            prev = curr
        sub_end.next = p2
        p1.next = curr
        return new_head.next
            
            

    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 1
        pointer = head
        while pointer.next:
            n +=1
            pointer=pointer.next
        
        newk = k%n
        if newk==0:
            return head
        else:
            p1 = head
            for i in range(n-newk-1):
                p1=p1.next
            newhead = p1.next
            p1.next=None
            pointer.next = head
            return newhead

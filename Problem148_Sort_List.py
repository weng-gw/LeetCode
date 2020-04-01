# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## top down (recursive) implementation with O(log(n)) space
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head),self.sortList(mid))
        
    def merge(self,h1,h2):
        dummy = ListNode(0)
        tail = dummy
        while h1 and h2:
            if h1.val>h2.val:
                h1,h2 = h2,h1
            tail.next = h1
            h1 = h1.next
            tail = tail.next
        tail.next = h1 if h1 else h2
        return dummy.next
    


## bottom up implementation with O(1) space
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        L=0
        while curr:
            L+=1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        n = 1
        while n<L:
            curr = dummy.next
            tail = dummy
            while curr:
                l = curr
                r = self.split(curr,n)
                curr = self.split(r,n)
                merged = self.merge(l,r)
                tail.next = merged[0]
                tail = merged[1]
            n*=2
        return dummy.next
    
    def split(self,head,n):
        while n>1 and head:
            head = head.next
            n-=1
        rest = head.next if head else None
        if head:
            head.next = None
        return rest
                
    def merge(self,h1,h2):
        dummy = ListNode(0)
        tail = dummy
        while h1 and h2:
            if h1.val>h2.val:
                h1,h2 = h2,h1
            tail.next = h1
            h1 = h1.next
            tail = tail.next
        tail.next = h1 if h1 else h2
        while tail.next:
            tail = tail.next
        return dummy.next,tail

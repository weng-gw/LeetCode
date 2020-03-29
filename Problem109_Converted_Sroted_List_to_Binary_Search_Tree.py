# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findsize(head):
            p = head
            count = 0
            while p:
                count+=1
                p=p.next
            return count
        size = findsize(head)
        def convert(l,r):
                nonlocal head
                if l >r:
                    return None
                mid = (l+r)//2
                
                left = convert(l,mid-1)
                
                node = TreeNode(head.val)
                node.left =left
                
                head = head.next
                
                node.right  = convert(mid+1,r)
                return node
        return convert(0,size-1)
            

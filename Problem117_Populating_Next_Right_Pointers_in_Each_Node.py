"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        mydq = collections.deque([root,None])
        count=1
        while count:
            current = mydq.popleft()
            newcount = 0
            for i in range(count):
                node = mydq.popleft()
                current.next = node
                if current.left:
                    mydq.append(current.left)
                    newcount+=1
                if current.right:
                    mydq.append(current.right)
                    newcount+=1
                current=node
            mydq.append(None)
            count=newcount
        return root
            
        

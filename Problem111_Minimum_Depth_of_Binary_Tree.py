# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        mydq = deque([root])
        count=1
        depth=1
        while mydq:
            newcount = 0
            for i in range(count):
                node = mydq.pop()
                if (not node.left) and (not node.right):
                    return depth
                if node.left:
                    mydq.appendleft(node.left)
                    newcount+=1
                if node.right:
                    mydq.appendleft(node.right)
                    newcount+=1
            count = newcount
            depth+=1

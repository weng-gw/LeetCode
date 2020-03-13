# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        mydq = deque()
        mydq.append(root)
        n = 1
        while(mydq):
            count = 0
            out = []
            for i in range(n):
                node = mydq.popleft()
                out.append(node.val)
                if node.left:
                    mydq.append(node.left)
                    count+=1
                if node.right:
                    mydq.append(node.right)
                    count+=1
            ans.append(out)
            n = count
        return ans

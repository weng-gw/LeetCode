# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        mydq = deque()
        mydq.append(root)
        n = 1
        direction = 1
        while(mydq):
            count = 0
            out = []
            if direction==1:
                for i in range(n):
                    node = mydq.popleft()
                    out.append(node.val)
                    if node.left:
                        mydq.append(node.left)
                        count+=1
                    if node.right:
                        mydq.append(node.right)
                        count+=1
            else:
                for i in range(n):
                    node = mydq.pop()
                    out.append(node.val)
                    if node.right:
                        mydq.appendleft(node.right)
                        count+=1
                    if node.left:
                        mydq.appendleft(node.left)
                        count+=1
            ans.append(out)
            n = count
            direction *=-1            
        return ans

        

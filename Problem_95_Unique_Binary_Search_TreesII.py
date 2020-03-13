# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(l,r):
            if l==r:
                return [None]
            out=[]
            for i in range(l,r):
                for left in generate(l,i):
                    for right in generate(i+1,r):
                        root = TreeNode(i+1)
                        root.left = left
                        root.right = right
                        out.append(root)
            return out
        return generate(0,n) if n else []

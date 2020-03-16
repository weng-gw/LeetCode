# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        if len(inorder) != len(postorder):
            return None
        def build(istart,iend,pstart,pend):
            if pstart>pend:
                return None
            root = TreeNode(postorder[pend])
            im = mydic[postorder[pend]]
            pm = pend-(iend-im)
            root.left = build(istart,im-1,pstart,pm-1)
            root.right = build(im+1,iend,pm,pend-1)
            return root
        mydic = {}
        for i in range(len(inorder)):
            mydic[inorder[i]] = i
        return build(0,len(inorder)-1,0,len(postorder)-1)

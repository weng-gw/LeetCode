# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None
        def build(istart,iend,pstart,pend,preorder,inorder,mydic):
            if pstart>pend:
                return None
            root = TreeNode(preorder[pstart])
            im = mydic[preorder[pstart]]
            pm = pstart +(im-istart)
            root.left = build(istart,im-1,pstart+1,pm,preorder,inorder,mydic)
            root.right = build(im+1,iend,pm+1,pend,preorder,inorder,mydic)
            return root
        mydic = {}
        for i in range(len(inorder)):
            mydic[inorder[i]] = i
        return build(0,len(inorder)-1,0,len(preorder)-1,preorder,inorder,mydic)

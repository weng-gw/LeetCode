# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        def dfs(node,s,ans,out):
            if not node.left and not node.right:
                if sum(ans)==s:
                    out.append(list(ans))
                    return
            if node.left:
                ans.append(node.left.val)
                dfs(node.left,s,ans,out)
                ans.pop()
            if node.right:
                ans.append(node.right.val)
                dfs(node.right,s,ans,out)
                ans.pop()
        if not root:
            return []
        out=[]
        ans=[root.val]
        dfs(root,s,ans,out)
        return out
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            if node.val<=lower or node.val >=upper:
                return False
            
            if not isValid(node.left,lower,node.val):
                return False
            if not isValid(node.right,node.val,upper):
                return False
            return True
        return isValid(root)

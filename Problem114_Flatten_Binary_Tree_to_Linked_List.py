# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root.left and not root.right:
                return root
            elif not root.left:
                return helper(root.right)                
            elif not root.right:
                root.right = root.left
                root.left=None
                return helper(root.right)
            else:
                leftend = helper(root.left)
                rightend = helper(root.right)
                leftend.right = root.right
                root.right=root.left
                root.left=None
                return rightend
                
        if not root:
            return root
        helper(root)

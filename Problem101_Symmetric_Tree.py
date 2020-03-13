# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## recursive solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(p,q):
            if not p or not q:
                return p==q
            if p.val != q.val:
                return False
            if not is_mirror(p.left,q.right):
                return False
            if not is_mirror(p.right,q.left):
                return False
            return True
        if not root:
            return True
        return is_mirror(root.left,root.right)

## iteration solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(p,q):
            qstack = [p]
            pstack = [q]
            while qstack or pstack:
                pnode =pstack.pop()
                qnode = qstack.pop()
                if not pnode and not qnode:
                    continue
                if not pnode or not qnode:
                    return False
                if pnode.val != qnode.val:
                    return False
                pstack.append(pnode.left)
                pstack.append(pnode.right)
                qstack.append(qnode.right)
                qstack.append(qnode.left)
            return True                
        if not root:
            return True
        return is_mirror(root.left,root.right)

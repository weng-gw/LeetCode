# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def construct(start,end):
            if start>end:
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = construct(start,mid-1)
            root.right = construct(mid+1,end)
            return root
        return construct(0,len(nums)-1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,start,end,k,ans,out):
            if len(ans)==k:
                out.append(list(ans))
                return
            for i in range(start,end+1):
                ans.append(nums[i])
                dfs(nums,i+1,end,k,ans,out)
                ans.pop()
        out=[]
        for k in range(len(nums)+1):
            dfs(nums,0,len(nums)-1,k,[],out)  
        return out

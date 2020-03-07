class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,start,end,k,ans,out):
            if len(ans)==k:
                out.add(tuple(ans))
                return
            for i in range(start,end+2-(k-len(ans))):
                ans.append(nums[i])
                dfs(nums,i+1,end,k,ans,out)
                ans.pop()
        nums.sort()
        out=set()
        for k in range(len(nums)+1):
            dfs(nums,0,len(nums)-1,k,[],out)
        return out
                

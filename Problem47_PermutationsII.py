class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,n,used,curr,ans):
            if len(curr)==n:
                ans.append(list(curr))
                return
            num_set = set()
            for i in range(n):
                if used[i]:
                    continue
                if nums[i] in num_set:
                    continue
                num_set.add(nums[i])
                curr.append(nums[i])
                used[i]=True
                dfs(nums,n,used,curr,ans)
                curr.pop()
                used[i]=False
        ans=[]
        used=[False]*len(nums)
        dfs(nums,len(nums),used,[],ans)
        return ans

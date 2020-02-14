class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,n,used,curr,ans):
            if len(curr)==n:
                ans.append(list(curr))
                return
            for i in range(n):
                if used[i]:
                    continue
                else:
                    curr.append(nums[i])
                    used[i] = True
                    dfs(nums,n,used,curr,ans)
                    used[i]=False
                    curr.pop()
        ans =[]
        used=[False]*len(nums)
        dfs(nums,len(nums),used,[],ans)
        return ans

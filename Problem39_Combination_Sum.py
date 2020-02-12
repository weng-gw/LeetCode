class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.dfs(candidates,target,0,[],ans)
        return ans
        
        
    def dfs(self,candidates,target, s,curr,ans):
        if target==0:
            ans.append(curr)
            return
        for i in range(s,len(candidates)):
            if candidates[i]>target:
                return
            self.dfs(candidates,target-candidates[i],i,curr+[candidates[i]],ans)



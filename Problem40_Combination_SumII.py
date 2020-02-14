class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def dfs(candidates, target, s,n, curr, ans):
            if target==0:
                ans.add(tuple(curr))
            for i in range(s,n):
                if candidates[i]> target:
                    return
                curr.append(candidates[i])
                dfs(candidates,target-candidates[i],i+1,n,list(curr),ans)
                curr.pop()
        dfs(candidates,target,0,len(candidates),[],ans)
        return ans

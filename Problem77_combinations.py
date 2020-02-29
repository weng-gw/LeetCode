class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start,end,k,ans,out):
            if len(ans)==k:
                out.append(list(ans))
                return
            for i in range(start,end+1):
                ans.append(i)
                dfs(i+1,end,k,ans,out)
                ans.pop()
        out=[]
        dfs(1,n,k,[],out)
        return out

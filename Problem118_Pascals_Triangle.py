class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        out = [[1],[1,1]]
        for i in range(3,numRows+1):
            ans = [1]*i
            for j in range(1,i-1):
                ans[j] = out[-1][j-1]+out[-1][j]
            out.append(ans)
        return out
        

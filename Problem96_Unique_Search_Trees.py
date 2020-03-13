class Solution:
    def numTrees(self, n: int) -> int:
        def count_bst(n,out):
            out[0]=1
            out[1]=1
            for i in range(2,n+1):
                count =0
                for j in range(1,i+1):
                    count += out[j-1]*out[i-j]
                out[i]=count
        out = [0]*(n+1)
        count_bst(n,out)
        return out[-1]

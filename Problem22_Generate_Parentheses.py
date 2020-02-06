class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrace(S='',left=0,right=0):
            if len(S)==2*n:
                ans.append(S)
                return
            if left < n:
                backtrace(S+"(",left=left+1,right = right)
            if right <left:
                backtrace(S+")",left=left,right = right+1)
        backtrace()
        return ans
                

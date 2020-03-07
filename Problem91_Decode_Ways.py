class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        out = [0]*n
        out[-1] = 1 if s[n-1]!="0" else 0
        if n==1:
            return out[0]
        if s[n-2]=="0":
            out[-2]=0
        elif s[n-1]=="0":
            out[-2] = 1 if int(s[(n-2):n])<=26 else 0
        else:
            out[-2] = 2 if int(s[(n-2):n])<=26 else 1
        if n==2:
            return out[0]
        for i in range(n-3,-1,-1):
            if s[i]=="0":
                out[i]=0
            else:
                out[i] = out[i+1]+(int(s[i:(i+2)])<=26)*out[i+2]
        return out[0]

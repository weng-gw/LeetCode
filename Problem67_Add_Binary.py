class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a = len(a)
        n_b = len(b)
        long_s, short_s = (a,b) if n_a>=n_b else (b,a)
        out = []
        remain = 0
        for i in range(-1,-len(short_s)-1,-1):
            remain,val = divmod(remain+int(long_s[i])+int(short_s[i]),2)
            out.append(str(val))
        for i in range(-len(short_s)-1,-len(long_s)-1,-1):
            remain,val = divmod(remain+int(long_s[i]),2)
            out.append(str(val))
        if remain==1:
            out.append(str(1))
        out.reverse()
        return "".join(out)

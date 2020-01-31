class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2*numRows -2
        strlist = []
        for i in range(numRows):
            for j in range(i,n,cycle):
                strlist.append(s[j])
                if i!=0 and i!=numRows-1 and j+cycle-2*i<n:
                    strlist.append(s[j+cycle-2*i])
        return "".join(strlist)
        

class Solution:
    def titleToNumber(self, s: str) -> int:
        out = 0
        for c in s:
            out = out*26+(ord(c)-ord("A")+1)
        return out
            
        

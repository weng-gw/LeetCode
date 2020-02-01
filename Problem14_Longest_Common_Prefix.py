class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        if not strs:
            return out
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[0][i]!=strs[j][i]:
                        return out
            out +=strs[0][i]
        return out
                        

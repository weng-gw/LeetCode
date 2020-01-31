class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            len3 = max(len1,len2)
            if len3 >end-start:
                start = i -(len3-1)//2
                end = i+len3//2
        return s[start:(end+1)]
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >=0 and R < len(s) and s[L]==s[R]:
            L -=1
            R +=1
        return R-L-1

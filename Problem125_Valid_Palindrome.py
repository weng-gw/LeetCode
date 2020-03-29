class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news =[]
        for c in s:
            if ord("a")<=ord(c)<=ord("z") or ord("0")<=ord(c)<=ord("9"):
                news.append(c)
        n = len(news)
        for i in range(n//2):
            if news[i]!=news[n-1-i]:
                return False
        return True
        

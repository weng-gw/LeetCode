class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        lower_start = ord("a")
        lower_end = ord("z")
        higher_start = ord("A")
        higher_end = ord("Z")
        while n>=1 and (not lower_start<=ord(s[n-1])<=lower_end) and (not higher_start<=ord(s[n-1])<=higher_end):
            n = n-1
        if n==0:
            return 0
        count = 1
        m = n-1
        while m>=1 and ( lower_start<=ord(s[m-1])<=lower_end or higher_start<=ord(s[m-1])<=higher_end):
            m = m-1
            count+=1
        return count

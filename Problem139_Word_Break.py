class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(s,wordset,mem):
            n = len(s)
            if mem[n-1]is not None:
                return mem[n-1]
            if s in wordset:
                mem[n-1]=True
                return mem[n-1]
            for i in range(n-1):
                first = s[:(i+1)]
                second = s[(i+1):]
                if dp(first,wordset,mem) and second in wordset:
                    mem[n-1]=True
                    return True
            mem[n-1]=False
            return False
        wordset = set(wordDict)
        mem = [None]*len(s)
        return dp(s,wordset,mem)

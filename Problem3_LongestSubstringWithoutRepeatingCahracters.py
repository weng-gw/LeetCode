class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        myset = set()
        i = 0
        j = 0
        counter = 0
        max_count = 0
        while j < len(s):
            if s[j] not in myset:
                myset.add(s[j])
                counter += 1
                j += 1
                max_count = max(max_count,counter)
            else:
                myset.remove(s[i])
                counter -= 1
                i += 1
        return max_count                

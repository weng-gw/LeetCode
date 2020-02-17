class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_code(string):
            start = ord("a")
            code = [0]*26
            for c in string:
                code[ord(c)-start]+=1
            return tuple(code)
        mydic = {}
        for s in strs:
            code = get_code(s)
            if code in mydic:
                mydic[code].append(s)
            else:
                mydic[code] = [s]
        return mydic.values()

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mydic = {"2":"abc",
                 "3":"def",
                 "4":"ghi",
                 "5":"jkl",
                 "6":"mno",
                 "7":"pqrs",
                 "8":"tuv",
                 "9":"wxyz"}
        if not digits:
            return []
        if len(digits)==1:
            return list(mydic[digits])
        s = digits[-1]
        out = []
        short_out = self.letterCombinations(digits[:-1])
        for c in mydic[s]:
            for i in short_out:
                out.append(i+c)
        return out

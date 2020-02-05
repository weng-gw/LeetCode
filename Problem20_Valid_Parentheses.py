class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack =[]
        mydic={")":"(","]":"[","}":"{"}
        for c in s:
            if c=="(" or c=="[" or c=="{":
                stack.append(c)
            elif not stack:
                return False
            else:
                last = stack.pop()
                if last != mydic[c]:
                    return False
        return True if not stack else False

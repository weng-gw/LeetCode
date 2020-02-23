from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n<1:
            return ""
        out =""
        nums=list(range(1,n+1))
        fact = factorial(n-1)
        size = n
        while size>=2:
            idx = (k-1)//fact
            out+=str(nums[idx])
            k = k%fact
            nums.pop(idx)
            size -= 1
            fact = int(fact/size)
        out+=str(nums[0])
        return out

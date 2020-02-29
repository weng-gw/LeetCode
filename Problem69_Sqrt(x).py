class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        start=0
        end = x
        while end>start+1:
            mid = (start+end)//2
            if mid**2==x:
                return mid
            if mid**2 <x:
                start = mid
            else:
                end = mid
        return start

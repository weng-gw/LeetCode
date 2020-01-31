class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        ans = 0
        while abs_x%10>0 or abs_x//10 >0:
            ans = ans*10+abs_x%10
            abs_x = abs_x//10
        if ans>= 2**31:
            return 0
        return ans if x>0 else -ans
            

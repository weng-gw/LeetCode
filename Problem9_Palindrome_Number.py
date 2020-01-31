class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse_x = self.reverse(x)
        return x==reverse_x
        
        
    def reverse(self,x):
        out = 0
        while x>0:
            out = out*10+x%10
            x = x//10
        return out
        
    

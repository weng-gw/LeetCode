class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = n
        count2 = 0
        while num:
            num = num//2
            count2+=num
        num = n
        count5 = 0
        while num:
            num = num//5
            count5+=num
        return min(count2,count5)
        
            

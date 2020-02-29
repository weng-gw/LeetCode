from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = n//2
        count=0
        for i in range(n2+1):
            n1 = n-i*2
            count+=factorial(n1+i)/factorial(n1)/factorial(i)
        return int(count)

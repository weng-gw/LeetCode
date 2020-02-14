class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        n1 = len(num1)
        n2 = len(num2)
        for i,c1 in enumerate(num1):
            ans_temp = 0
            for j,c2 in enumerate(num2):
                ans_temp+=int(c1)*int(c2)*(10**(n2-j-1))
            ans+=ans_temp*(10**(n1-i-1))
        return str(ans)
    

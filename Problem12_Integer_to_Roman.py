class Solution:
    def intToRoman(self, num: int) -> str:
        out = []
        val = num
        symbol = "IVXLCDMM"
        for i in range(4):
            res = num%10
            start = i*2
            out.append(self.one_digit(res,symbol[start:(start+3)]))
            num = num//10
        return "".join(out[::-1])
            
        
    def one_digit(self,num,s):
        if num==0:
            return ""
        if num <= 3:
            return s[0]*num
        if num ==4:
            return s[0]+s[1]
        if num==5:
            return s[1]
        if num<=8:
            return s[1]+(num-5)*s[0]
        return s[0]+s[2]

class Solution:
    def romanToInt(self, s: str) -> int:
        mydic={"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        I_deduct=0
        C_deduct = 0
        X_deduct = 0
        
        value = 0
        for i in range(len(s)):
            value+=mydic[s[i]]
            if s[i]=="I" and i < len(s)-1 and (s[i+1]== "V" or s[i+1]=="X"):
                I_deduct += mydic["I"]
            if s[i]=="C" and i < len(s)-1 and (s[i+1]== "D" or s[i+1]=="M"):
                C_deduct += mydic["C"]
            if s[i]=="X" and i < len(s)-1 and (s[i+1]== "L" or s[i+1]=="C"):
                X_deduct += mydic["X"]
        value -= 2*I_deduct+2*C_deduct+2*X_deduct
        return value

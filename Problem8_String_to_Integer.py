class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str)==0:
            return 0
        out = []
        sign_flag =0
        sign = 1
        num_flag=0
        for s in str:
            if s==" ":
                if num_flag==0 and sign_flag==0:
                    continue
                else:
                    break
            if s=="-":
                if sign_flag==0:
                    sign=-1
                    sign_flag=1
                else:
                    break
            elif s=="+":
                if sign_flag==0:
                    sign=1
                    sign_flag=1
                else:
                    break        
            elif (ord(s)<=ord('9') and ord(s)>= ord('0')):
                out.append(s)
                num_flag=1
                sign_flag=1
            else:
                break
        if out:
            val = int("".join(out))
            if val>= 2**31:
                return 2**31-1 if sign >0 else -(2**31)
            return sign*val
        else:
            return 0

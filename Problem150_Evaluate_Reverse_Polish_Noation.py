class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return a+b
        def subtract(a,b):
            return a-b
        def multiply(a,b):
            return a*b
        def divide(a,b):
            return int(a/b)
        fun_dic = { "+":add,
                    "-":subtract,
                    "*":multiply,
                    "/":divide
        }
        stack = []
        for s in tokens:
            if s not in fun_dic:
                stack.append(int(s))
            else:
                b = stack.pop()
                a = stack.pop()
                c = fun_dic[s](a,b)
                stack.append(c)
        return  stack.pop()
                
        

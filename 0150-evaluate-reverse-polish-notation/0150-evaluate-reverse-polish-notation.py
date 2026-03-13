class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            if token not in '+-*/':
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                
                if token == '+':
                    res = op1 + op2
                elif token == '-':
                    res = op1 - op2
                elif token == '*':
                    res = op1 * op2
                elif token == '/':
                    res = int(op1 / op2)
                
                stack.append(res)

        return stack[-1]
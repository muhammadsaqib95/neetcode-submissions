class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+' : '+',
            '-' : '-',
            '*' : '*',
            '/' : '/',
        }

        for s in tokens:
            if s in operations:
                s1 = stack.pop();
                s2 = stack.pop();
                match s:
                    case '+':
                        r = s1 + s2
                    case '-':
                        r = s2 - s1
                    case '*':
                        r = s1 * s2
                    case '/':
                        r = int(s2 / s1)
                stack.append(r)
            else:
                stack.append(int(s))
        return stack[0]

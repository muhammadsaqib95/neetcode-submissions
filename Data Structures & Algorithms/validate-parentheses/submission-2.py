class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:return False
                lc = stack.pop()
                if closing[lc] != c:
                    return False
        return len(stack) == 0

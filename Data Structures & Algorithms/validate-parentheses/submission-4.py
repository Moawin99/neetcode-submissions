class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = [')', '}', ']']

        for a in s:
            if len(stack) == 0 and a in closed:
                return False
            elif a not in closed:
                stack.append(a)
            else:
                op = stack.pop()
                if a == ')' and op != '(':
                    return False
                elif a == '}' and op != '{':
                    return False
                elif a == ']' and op != '[':
                    return False
        return True and len(stack) == 0
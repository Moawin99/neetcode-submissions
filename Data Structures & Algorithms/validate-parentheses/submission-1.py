class Solution:
    def isValid(self, s: str) -> bool:
        Map = {'}': '{', ']': '[', ')': '('}
        stack = []

        for x in s:
            if x not in Map:
                stack.append(x)
                continue
            if not stack or stack[-1] != Map[x]:
                return False
            stack.pop()
        return not stack
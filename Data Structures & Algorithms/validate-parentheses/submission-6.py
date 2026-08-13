class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = { ')': '(', ']': '[', '}': '{'}

        for a in s:
            if a in closedToOpen:
                if stack and stack[-1] == closedToOpen[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        return True if not stack else False
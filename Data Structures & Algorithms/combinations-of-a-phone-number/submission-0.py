class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        stack = deque()
        phmap = {'2': ['a','b','c'], 
                 '3': ['d','e','f'],
                 '4': ['g','h','i'], 
                 '5': ['j','k','l'], 
                 '6': ['m','n','o'],
                 '7': ['p','q','r', 's'], 
                 '8': ['t','u','v'],
                 '9': ['w','x','y', 'z'],}
        
        i = 0
        # Init stack
        for x in phmap[digits[i]]:
            stack.append(x)
        i += 1

        while stack:
            if i == len(digits):
                break
            
            for j in range(len(stack)):
                tmp = stack.popleft()
                print(stack)
                lett = phmap[digits[i]]
                for x in lett:
                    tmp += x
                    stack.append(tmp)
                    tmp = tmp[:-1]
            i += 1

        return list(stack)

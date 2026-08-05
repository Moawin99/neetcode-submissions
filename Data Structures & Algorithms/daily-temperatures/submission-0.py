class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for l in range(len(temperatures)):
            if (l == len(temperatures) - 1):
                res.append(0)
                return res
            r = l + 1
            count = 1
            while r < len(temperatures):
                if (temperatures[r] > temperatures[l]):
                    res.append(count)
                    break
                elif (r == len(temperatures) - 1):
                    res.append(0)
                r += 1
                count += 1
            

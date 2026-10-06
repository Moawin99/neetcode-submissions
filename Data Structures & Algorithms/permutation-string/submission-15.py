class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aMap = {}
        A, B = s1, s2
        if len(s2) < len(s1):
            return False
        
        for x in A:
            aMap[x] = aMap.get(x, 0) + 1
        
        bMap = {}
        L = 0
        for i, x in enumerate(B):
            if x not in aMap:
                bMap = {}
                L += 1
            else:
                bMap[x] = bMap.get(x, 0) + 1
                if aMap == bMap:
                    return True
                while bMap[x] > aMap[x]:
                    ch = B[L]
                    bMap[ch] = bMap.get(ch) - 1
                    if bMap[ch] == 0:
                        del bMap[ch]
                    L += 1

                
        return False


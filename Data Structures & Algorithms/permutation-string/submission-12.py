class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        for x in s1:
            s1_map[x] = s1_map.get(x, 0) + 1
        
        l = 0
        s2_map = {}
        for y in s2:
            if y not in s1_map:
                while len(s2_map) != 0:
                    ele = s2[l]
                    s2_map[ele] = s2_map.get(ele) - 1
                    if s2_map[ele] == 0:
                        del s2_map[ele]
                    l += 1
                l += 1
                continue
            else:
                s2_map[y] = s2_map.get(y, 0) + 1
                if s1_map == s2_map:
                    return True
                else:
                    while s2_map[y] > s1_map[y]:
                        ele = s2[l]
                        s2_map[ele] = s2_map.get(ele) - 1
                        if s2_map[ele] == 0:
                            del s2_map[ele]
                        l += 1
        return False

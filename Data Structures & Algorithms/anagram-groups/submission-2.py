class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            cur = "".join(sorted(s))
            if cur not in m:
                m[cur] = []
            m[cur].append(s)
        
        return list(m.values())
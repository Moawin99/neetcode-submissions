class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for x in strs:
            if ''.join(sorted(x)) not in my_map:
                my_map[''.join(sorted(x))] = []
            my_map[''.join(sorted(x))].append(x)
        vals = []
        for values in list(my_map.values()):
            vals.append(values)
        return vals
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        j = 0
        while j < len(s):
            num = ""
            while s[j] != "#":
                num += s[j]
                j += 1
            word_len = int(num)
            res.append(s[j + 1: j + 1 + word_len])
            j = j + 1 + word_len
        
        return res
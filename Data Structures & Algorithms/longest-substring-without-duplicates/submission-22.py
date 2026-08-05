class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, L = 0, 0
        dup = set()

        for R in range(len(s)):
            if s[R] not in dup:
                dup.add(s[R])
                length = max(length, len(dup))
            else:
                while s[R] != s[L]:
                    dup.remove(s[L])
                    L += 1
                L += 1
        return length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub = set()

        l = 0

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            ans = max(ans, len(sub))
        return ans
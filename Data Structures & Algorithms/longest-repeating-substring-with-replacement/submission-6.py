class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        total, L = 0, 0
        letterMap = {}
        ans = 0

        for R in range(len(s)):
            letterMap[s[R]] = letterMap.get(s[R], 0) + 1
            freqLett = max(letterMap.values())
            total += 1
            if total - freqLett <= k:
                ans = max(ans, total)
            else:
                letterMap[s[L]] = letterMap[s[L]] - 1
                L += 1
                total -= 1
        return ans
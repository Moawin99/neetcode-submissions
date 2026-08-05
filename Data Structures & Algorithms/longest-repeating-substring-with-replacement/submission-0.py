class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        subString = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] not in subString:
                subString[s[r]] = 1
            else:
                subString[s[r]] = subString[s[r]] + 1
            
            max_appear_num = max(subString.values())
            total = sum(subString.values())
            if total - max_appear_num > k:
                subString[s[l]] = subString[s[l]] - 1
                total -= 1
                l += 1
            ans = max(ans, total)
        return ans

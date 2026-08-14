class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_map = {}
        l = 0
        max_count = 0
        res = 0

        for x in s:
            max_map[x] = max_map.get(x, 0) + 1
            max_count = max(max_map.values())
            window_size = sum(max_map.values())
            while window_size - max_count > k:
                max_map[s[l]] = max_map.get(s[l]) - 1 
                max_count = max(max_map.values())
                window_size -= 1
                l += 1
            res = max(res, window_size)
        
        return res
            


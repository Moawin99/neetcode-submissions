class Solution:
    def trap(self, height: List[int]) -> int:
        ln = len(height)
        max_left = [0] * ln
        max_right = [0] * ln

        max_left[0] = height[0]
        for i, h in enumerate(height):
            if i > 0:
                max_left[i] = max(max_left[i - 1], h)
        
        max_right[-1] = height[-1]
        for i in range(ln-1, -1, -1):
            h = height[i]
            if i < ln-1:
                max_right[i] = max(max_right[i + 1], h)
        
        ans = 0
        for i, h in enumerate(height):
            min_h = min(max_left[i], max_right[i])
            if h < min_h:
                ans += min_h - h
        return ans
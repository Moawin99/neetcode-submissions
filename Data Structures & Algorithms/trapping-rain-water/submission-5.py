class Solution:
    def trap(self, height: List[int]) -> int:
        lh = len(height)
        max_left = [0] * lh
        max_right = [0] * lh

        max_left[0] = height[0]
        for i, h in enumerate(height):
            if i > 0:
                max_left[i] = max(max_left[i - 1], h)
        
        max_right[-1] = height[-1]
        for i in range(lh - 1, -1, -1):
            h = height[i]
            if i < lh - 1:
                max_right[i] = max(max_right[i + 1], h)
        
        area = 0
        for i, h in enumerate(height):
            gap = min(max_left[i], max_right[i])
            if h < gap:
                area += gap - h
        return area
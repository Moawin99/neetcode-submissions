class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        L, R = 0, len(heights) - 1

        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
            max_area = max(max_area, area)
        
        return max_area
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        sub = []

        for x in nums:
            sub.append(x)
            sub_Tot = sum(sub)
            total = max(total, sub_Tot)
            if sub_Tot < 0:
                sub.clear()
        
        return total

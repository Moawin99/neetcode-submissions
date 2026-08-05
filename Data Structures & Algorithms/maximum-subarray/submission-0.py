class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = n + max(curSum, 0)
            maxSum = max(maxSum, curSum)
        return maxSum
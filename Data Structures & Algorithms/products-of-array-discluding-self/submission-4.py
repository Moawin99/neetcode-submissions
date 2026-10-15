class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [0] * size
        postfix = [0] * size
        res = [0] * size

        prefix[0] = postfix[size-1] = 1
        for i in range(1, size):
            prefix[i] = nums[i-1] * prefix[i - 1]
        
        for i in range(size - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        for i in range(size):
            res[i] = prefix[i] * postfix[i]
        
        return res
            
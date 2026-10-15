class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [0] * size
        postfix = [0] * size
        res = [0] * size

        # build prefix arr
        for i in range(size):
            if i == 0:
                prefix[0] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]
        
        # build prefix arr
        for i in range(size - 1, 0, -1):
            if i == size - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]
        
        for i in range(size):
            if i == 0:
                res[i] = 1 * postfix[i + 1]
            elif i == size - 1:
                res[i] = prefix[i - 1] * 1
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res
            
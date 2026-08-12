class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multp = 1
        zero_counter = 0
        for x in nums:
            if x == 0:
                zero_counter += 1
                continue
            multp *= x
        
        if zero_counter >= 2:
            return [x*0 for x in range(len(nums))]

        products = []
        for x in nums:
            if x != 0 and zero_counter == 1:
                products.append(0)
            elif x == 0 and zero_counter == 1:
                products.append(multp)
            else:
                products.append(int(multp/x))
        return products
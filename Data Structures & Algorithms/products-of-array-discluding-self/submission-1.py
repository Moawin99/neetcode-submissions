class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCounter = 0
        for x in nums:
            if x == 0:
                zeroCounter += 1
                continue
            total *= x
        ans = []
        if zeroCounter > 1:
            return [x*0 for x in range(len(nums))]

        for x in nums:
            if x != 0 and zeroCounter == 1:
                ans.append(0)
            elif x == 0 and zeroCounter == 1:
                ans.append(total)
            else:
                ans.append(int(total/x))
        return ans

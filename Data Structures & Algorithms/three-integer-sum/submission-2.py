class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, x in enumerate(nums):
            # all nums are positive, no possible way to be 0
            if x > 0:
                break
            
            # if i > 0 and x == nums[i-1]:
            #     continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = x + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    trip = sorted([x, nums[l], nums[r]])
                    if trip not in res:
                        res.append(trip)
                    l += 1
                    r -= 1
        return res

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            k = (l + r) // 2
            if nums[k] == target:
                return k
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if nums[k] < nums[l]:
                if nums[k] < target < nums[r]:
                    l = k + 1
                else:
                    r = k - 1
            else:
                if nums[l] < target < nums[k]:
                    r = k - 1
                else:
                    l = k + 1
        return res
